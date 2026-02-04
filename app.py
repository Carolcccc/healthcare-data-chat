import streamlit as st
import pandas as pd
from tools import create_agent
from prompts import SYSTEM_PROMPT

# Page configuration
st.set_page_config(
    page_title="Healthcare AI Agent",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .agent-message {
        background-color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'df' not in st.session_state:
    st.session_state.df = None

def initialize_agent():
    """Initialize the AI agent with the healthcare dataset"""
    try:
        csv_path = "healthcare_dataset_cleaned.csv"
        st.session_state.df = pd.read_csv(csv_path)
        st.session_state.agent = create_agent(csv_path)
        return True
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        return False

# Header
st.title("🏥 Healthcare AI Agent")
st.markdown("### Powered by Llama 3.2 on M4")

# Important Disclaimer
st.warning("""
⚠️ **IMPORTANT DISCLAIMER**: This is an educational tool for data analysis only. 
It does NOT provide medical advice. Always consult qualified healthcare professionals 
for medical decisions. AI responses may be inaccurate.
""")

# Sidebar
with st.sidebar:
    st.header("📊 Dataset Information")
    
    if st.button("🔄 Initialize Agent", type="primary"):
        with st.spinner("Loading healthcare dataset..."):
            if initialize_agent():
                st.success("✅ Agent initialized successfully!")
    
    if st.session_state.df is not None:
        st.metric("Total Records", len(st.session_state.df))
        st.metric("Total Columns", len(st.session_state.df.columns))
        
        with st.expander("📋 Dataset Preview"):
            st.dataframe(st.session_state.df.head(10), use_container_width=True)
        
        with st.expander("📈 Column Names"):
            for col in st.session_state.df.columns:
                st.text(f"• {col}")
    
    st.divider()
    
    st.header("💡 Example Questions")
    example_questions = [
        "What is the average age of patients?",
        "How many patients have Diabetes?",
        "What is the most common medical condition?",
        "Show me the distribution of blood types",
        "What is the average billing amount?",
        "How many patients are admitted?",
    ]
    
    for question in example_questions:
        if st.button(question, key=f"example_{question}", use_container_width=True):
            st.session_state.current_question = question
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Main content
if st.session_state.agent is None:
    st.info("👈 Click 'Initialize Agent' in the sidebar to get started!")
    st.markdown("""
    ### About This App
    
    This healthcare AI agent uses **Llama 3.2** running locally on your M4 Mac to analyze healthcare data.
    
    **Features:**
    - 🤖 Local AI execution (no API keys needed)
    - 📊 Interactive data analysis
    - 💬 Natural language queries
    - 📈 Real-time insights
    
    **How to use:**
    1. Initialize the agent using the sidebar button
    2. Ask questions about the healthcare dataset
    3. Get instant AI-powered answers
    """)
else:
    # Chat interface
    st.markdown("### 💬 Chat with the Agent")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for i, message in enumerate(st.session_state.chat_history):
            if message['role'] == 'user':
                st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You:</strong> {message['content']}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="chat-message agent-message">
                        <strong>🤖 Agent:</strong> {message['content']}
                    </div>
                """, unsafe_allow_html=True)
    
    # Input form
    with st.form(key="question_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_question = st.text_input(
                "Ask a question about the healthcare data:",
                placeholder="e.g., What is the average age of patients with Diabetes?",
                label_visibility="collapsed",
                key="user_input"
            )
        
        with col2:
            submit_button = st.form_submit_button("Send 🚀", use_container_width=True)
    
    # Handle form submission or example question
    question_to_process = None
    if submit_button and user_question:
        question_to_process = user_question
    elif hasattr(st.session_state, 'current_question'):
        question_to_process = st.session_state.current_question
        delattr(st.session_state, 'current_question')
    
    if question_to_process:
        # Add user message to chat history
        st.session_state.chat_history.append({
            'role': 'user',
            'content': question_to_process
        })
        
        # Get agent response
        with st.spinner("🤔 Thinking..."):
            try:
                full_query = f"{SYSTEM_PROMPT}\n\nUser Question: {question_to_process}"
                response = st.session_state.agent.invoke(full_query)
                agent_response = response['output']
                
                # Add agent response to chat history
                st.session_state.chat_history.append({
                    'role': 'agent',
                    'content': agent_response
                })
                
            except Exception as e:
                error_message = f"Error: {str(e)}"
                st.session_state.chat_history.append({
                    'role': 'agent',
                    'content': error_message
                })
        
        st.rerun()

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <small>Healthcare AI Agent • Running Llama 3.2 locally on M4 Mac • Built with Streamlit & LangChain</small>
        <br>
        <small style='color: #999;'>Educational Use Only • Not for Medical Diagnosis or Treatment • No Warranty Provided</small>
    </div>
""", unsafe_allow_html=True)
