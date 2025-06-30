
# 4-Layer Prompt Design

## 1. Input Understanding
Prompt: "User enters subject, topic, and confidence level. Extract intent and context."  
Purpose: Understand user need and set tone for personalization.

## 2. State Tracker
Prompt: "Store subject, topic, and confidence level. Recall for adaptive learning."  
Simulated using summary variables (topic_log, confidence_level).

## 3. Task Planner
Prompt: "Generate 3 questions. If confidence = low, add a memory trick. If performance = high, recommend next topic."  
Chaining and branching used.

## 4. Output Generator
Prompt: "Present questions one at a time. Use markdown. Offer option to continue or review answers."  
Formatting: numbered bullets, supportive tone, bold topic headings.
