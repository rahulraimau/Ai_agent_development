
# 🧠 AI Agent Assignment – Rahul Rai

## Use Case: AI Agent to Help Students Revise for Exams

### 🧾 SECTION 1: BASIC DETAILS
**Name:** Rahul Rai  
**AI Agent Title / Use Case:** AI Agent to Help Students Revise for Exams

### 🧠 SECTION 2: PROBLEM FRAMING
**2.1 What problem does your AI Agent solve?**  
Students struggle to revise efficiently. This agent helps them focus on weak topics and test their understanding.

**2.2 Why is this agent useful?**  
It guides revision by generating questions, memory tricks, and progress-based feedback.

**2.3 Who is the target user?**  
College students revising for exams in subjects like science, math, or history.

**2.4 What not to include?**  
Full lectures, long explanations, or grade predictions.

### 🧱 SECTION 3: 4-LAYER PROMPT DESIGN
**3.1 Input Understanding Prompt:**  
“User provides subject, topic, and confidence level. Extract and interpret what they want to revise.”

**3.2 State Tracker Prompt:**  
“Store the user’s subject, topic, and confidence level to simulate memory and tailor follow-ups.”

**3.3 Task Planner Prompt:**  
“Plan: generate 3 quiz questions → memory tip if confidence is low → track performance → suggest next topic.”

**3.4 Output Generator Prompt:**  
“Present questions with clear formatting, ask if user wants to check answer or continue.”

### 🔍 SECTION 4: CHATGPT EXPLORATION LOG
| Attempt | Prompt Variant | What Happened | What You Changed | Why You Changed It |
|--------|----------------|----------------|------------------|---------------------|
| 1 | Basic question gen | Generic output | Added confidence | Needed difficulty control |
| 2 | Add memory | GPT forgot context | Used state tracker vars | Simulate recall |
| 3 | Friendly tone | Too casual | Balanced tone | Keep clarity + empathy |

### 🧪 SECTION 5: OUTPUT TESTS
**Test 1:**  
Input: History – French Revolution – Medium  
Output: 3 relevant questions + follow-up prompt

**Test 2:**  
Input: “Math, not confident”  
Output: Request for topic + gentle tone

**Test 3:**  
Input: ""  
Output: “Let’s start with the subject.”

### 🔄 SECTION 6: REFLECTION
- Hardest: Simulating memory.  
- Most fun: Designing task flow logic.  
- Improvements: Add user-level tracking.  
- Learned: Structure > cleverness in prompt design.  
- Stuck?: Yes — solved by breaking into steps.

### 🧠 SECTION 7: HACK VALUE
- Used memory simulation and branching logic  
- Personalized difficulty and tone  
