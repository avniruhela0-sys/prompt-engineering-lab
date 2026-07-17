# 🔬 Prompt Engineering Lab

A hands-on exploration of different prompting styles using Google Gemini AI. This project tests 4 different prompting techniques on the same task to compare their effectiveness.

## 🎯 Task

Extract key information from a resume (name, contact, education, experience, skills, certifications).

## 🧪 Prompt Styles Tested

1. **Zero-Shot** - Direct instruction with no examples
2. **Few-Shot** - Provides 2 examples before the actual input
3. **Chain-of-Thought** - Requests step-by-step reasoning
4. **Structured JSON** - Requests specific JSON format output

## 📊 Results Summary

**Winner for this task:** Few-Shot Prompting (95% accuracy)

| Prompt Style | Accuracy | Best For |
|--------------|----------|----------|
| Few-Shot | 🏆 95% | Production use, consistent results |
| Chain-of-Thought | 90% | Complex reasoning, transparency |
| JSON Output | 90% | API integration |
| Zero-Shot | 85% | Quick tasks, simple extraction |

[📄 Read the full comparison →](RESULTS.md)

## 🚀 Installation

```bash
git clone https://github.com/avniruhela0-sys/prompt-engineering-lab.git
cd prompt-engineering-lab
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
