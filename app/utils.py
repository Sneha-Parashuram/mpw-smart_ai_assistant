import nltk
import random
import string

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ---------------------------------------------------
# DOWNLOAD REQUIRED NLTK DATA
# ---------------------------------------------------
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("vader_lexicon", quiet=True)

sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words("english"))

# ---------------------------------------------------
# 90 QUESTION DATASET (Technical + HR)
# ---------------------------------------------------

QUESTION_BANK = [

# =========================
# TECHNICAL — EASY (15)
# =========================
{
    "id": "tech_easy_1",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a variable in programming?",
    "keywords": ["variable", "store", "data"]
},
{
    "id": "tech_easy_2",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a function in programming?",
    "keywords": ["function", "reuse", "code"]
},
{
    "id": "tech_easy_3",
    "round": "technical",
    "difficulty": "easy",
    "question": "Explain the purpose of loops.",
    "keywords": ["loop", "repeat", "iteration"]
},
{
    "id": "tech_easy_4",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an array?",
    "keywords": ["array", "collection", "index"]
},
{
    "id": "tech_easy_5",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is debugging?",
    "keywords": ["debug", "error", "fix"]
},
{
    "id": "tech_easy_6",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an algorithm?",
    "keywords": ["algorithm", "steps", "solve"]
},
{
    "id": "tech_easy_7",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a data type?",
    "keywords": ["data", "type", "value"]
},
{
    "id": "tech_easy_8",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a compiler?",
    "keywords": ["compiler", "convert", "code"]
},
{
    "id": "tech_easy_9",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a boolean value?",
    "keywords": ["boolean", "true", "false"]
},
{
    "id": "tech_easy_10",
    "round": "technical",
    "difficulty": "easy",
    "question": "What does HTML stand for?",
    "keywords": ["html", "markup", "web"]
},
{
    "id": "tech_easy_11",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is CSS used for?",
    "keywords": ["css", "style", "design"]
},
{
    "id": "tech_easy_12",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is Git?",
    "keywords": ["git", "version", "control"]
},
{
    "id": "tech_easy_13",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an IDE?",
    "keywords": ["ide", "environment", "code"]
},
{
    "id": "tech_easy_14",
    "round": "technical",
    "difficulty": "easy",
    "question": "Define a class in OOP.",
    "keywords": ["class", "oop", "blueprint"]
},
{
    "id": "tech_easy_15",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a database?",
    "keywords": ["database", "store", "records"]
},


# =========================
# TECHNICAL — MEDIUM (15)
# =========================
{
    "id": "tech_med_1",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain the concept of recursion.",
    "keywords": ["recursion", "function", "call"]
},
{
    "id": "tech_med_2",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is polymorphism in OOP?",
    "keywords": ["oop", "polymorphism", "override"]
},
{
    "id": "tech_med_3",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is a REST API?",
    "keywords": ["rest", "api", "http"]
},
{
    "id": "tech_med_4",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain multithreading.",
    "keywords": ["thread", "parallel", "concurrency"]
},
{
    "id": "tech_med_5",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is SQL indexing?",
    "keywords": ["index", "query", "optimize"]
},
{
    "id": "tech_med_6",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is memory management?",
    "keywords": ["memory", "allocate", "free"]
},
{
    "id": "tech_med_7",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain inheritance in OOP.",
    "keywords": ["inheritance", "class", "extend"]
},
{
    "id": "tech_med_8",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is exception handling?",
    "keywords": ["exception", "try", "catch"]
},
{
    "id": "tech_med_9",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain how hashing works.",
    "keywords": ["hash", "collision", "map"]
},
{
    "id": "tech_med_10",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is a binary tree?",
    "keywords": ["tree", "node", "binary"]
},
{
    "id": "tech_med_11",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is Docker used for?",
    "keywords": ["docker", "container", "deploy"]
},
{
    "id": "tech_med_12",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain DNS and its purpose.",
    "keywords": ["dns", "domain", "resolve"]
},
{
    "id": "tech_med_13",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is virtual memory?",
    "keywords": ["virtual", "memory", "swap"]
},
{
    "id": "tech_med_14",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain API authentication.",
    "keywords": ["auth", "token", "secure"]
},
{
    "id": "tech_med_15",
    "round": "technical",
    "difficulty": "medium",
    "question": "Describe microservices architecture.",
    "keywords": ["microservices", "distributed", "services"]
},


# =========================
# TECHNICAL — HARD (15)
# =========================
{
    "id": "tech_hard_1",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain how operating systems handle deadlocks.",
    "keywords": ["deadlock", "os", "resource"]
},
{
    "id": "tech_hard_2",
    "round": "technical",
    "difficulty": "hard",
    "question": "What is ACID compliance in databases?",
    "keywords": ["acid", "transaction", "consistency"]
},
{
    "id": "tech_hard_3",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain time and space complexity of algorithms.",
    "keywords": ["complexity", "big o", "analysis"]
},
{
    "id": "tech_hard_4",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe load balancing algorithms.",
    "keywords": ["load", "balance", "algorithm"]
},
{
    "id": "tech_hard_5",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain distributed system consistency models.",
    "keywords": ["distributed", "consistency", "model"]
},
{
    "id": "tech_hard_6",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain the CAP theorem.",
    "keywords": ["cap", "consistency", "availability"]
},
{
    "id": "tech_hard_7",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain how garbage collection works.",
    "keywords": ["garbage", "memory", "collector"]
},
{
    "id": "tech_hard_8",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how a compiler optimizes code during compilation.",
    "keywords": ["compiler", "optimize", "code"]
},
{
    "id": "tech_hard_9",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain database sharding and replication.",
    "keywords": ["shard", "replica", "scale"]
},
{
    "id": "tech_hard_10",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how neural networks learn during training.",
    "keywords": ["neural", "train", "weights"]
},
{
    "id": "tech_hard_11",
    "round": "technical",
    "difficulty": "hard",
    "question": "What is a race condition and how can it be prevented?",
    "keywords": ["race", "thread", "lock"]
},
{
    "id": "tech_hard_12",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how a blockchain maintains trust.",
    "keywords": ["blockchain", "hash", "trust"]
},
{
    "id": "tech_hard_13",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain network congestion control algorithms.",
    "keywords": ["network", "congestion", "algorithm"]
},
{
    "id": "tech_hard_14",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain the internals of a virtual machine hypervisor.",
    "keywords": ["hypervisor", "vm", "virtual"]
},
{
    "id": "tech_hard_15",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe Paxos or Raft consensus algorithm.",
    "keywords": ["consensus", "raft", "paxos"]
},


# =========================
# HR — EASY (15)
# =========================
{
    "id": "hr_easy_1",
    "round": "hr",
    "difficulty": "easy",
    "question": "Tell me about yourself.",
    "keywords": ["intro", "background", "yourself"]
},
{
    "id": "hr_easy_2",
    "round": "hr",
    "difficulty": "easy",
    "question": "Why do you want this job?",
    "keywords": ["job", "reason", "motivation"]
},
{
    "id": "hr_easy_3",
    "round": "hr",
    "difficulty": "easy",
    "question": "What are your strengths?",
    "keywords": ["strength", "skill", "ability"]
},
{
    "id": "hr_easy_4",
    "round": "hr",
    "difficulty": "easy",
    "question": "Describe your weakness.",
    "keywords": ["weakness", "improve", "challenge"]
},
{
    "id": "hr_easy_5",
    "round": "hr",
    "difficulty": "easy",
    "question": "Where do you see yourself in five years?",
    "keywords": ["future", "plan", "career"]
},
{
    "id": "hr_easy_6",
    "round": "hr",
    "difficulty": "easy",
    "question": "What motivates you?",
    "keywords": ["motivate", "drive", "goal"]
},
{
    "id": "hr_easy_7",
    "round": "hr",
    "difficulty": "easy",
    "question": "Describe a time you worked in a team.",
    "keywords": ["team", "collaboration", "work"]
},
{
    "id": "hr_easy_8",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you handle stress?",
    "keywords": ["stress", "handle", "pressure"]
},
{
    "id": "hr_easy_9",
    "round": "hr",
    "difficulty": "easy",
    "question": "What do you know about our company?",
    "keywords": ["company", "research", "info"]
},
{
    "id": "hr_easy_10",
    "round": "hr",
    "difficulty": "easy",
    "question": "What hobbies do you have?",
    "keywords": ["hobby", "interest", "activity"]
},
{
    "id": "hr_easy_11",
    "round": "hr",
    "difficulty": "easy",
    "question": "Do you consider yourself a leader?",
    "keywords": ["leader", "leadership", "team"]
},
{
    "id": "hr_easy_12",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you stay organized?",
    "keywords": ["organized", "plan", "task"]
},
{
    "id": "hr_easy_13",
    "round": "hr",
    "difficulty": "easy",
    "question": "Tell me about a small achievement you are proud of.",
    "keywords": ["achievement", "proud", "goal"]
},
{
    "id": "hr_easy_14",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you adapt to new situations?",
    "keywords": ["adapt", "change", "flexible"]
},
{
    "id": "hr_easy_15",
    "round": "hr",
    "difficulty": "easy",
    "question": "Do you prefer working alone or in a team?",
    "keywords": ["team", "alone", "work"]
},


# =========================
# HR — MEDIUM (15)
# =========================
{
    "id": "hr_med_1",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a conflict you resolved at work or college.",
    "keywords": ["conflict", "resolve", "problem"]
},
{
    "id": "hr_med_2",
    "round": "hr",
    "difficulty": "medium",
    "question": "Explain how you respond to negative feedback.",
    "keywords": ["feedback", "improve", "response"]
},
{
    "id": "hr_med_3",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a time you showed leadership.",
    "keywords": ["leadership", "team", "initiative"]
},
{
    "id": "hr_med_4",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe your decision-making process.",
    "keywords": ["decision", "process", "choice"]
},
{
    "id": "hr_med_5",
    "round": "hr",
    "difficulty": "medium",
    "question": "What motivates you to perform well?",
    "keywords": ["motivate", "performance", "drive"]
},
{
    "id": "hr_med_6",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a risk you took and what happened.",
    "keywords": ["risk", "decision", "outcome"]
},
{
    "id": "hr_med_7",
    "round": "hr",
    "difficulty": "medium",
    "question": "How do you manage tight deadlines?",
    "keywords": ["deadline", "time", "stress"]
},
{
    "id": "hr_med_8",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a time you helped a struggling teammate.",
    "keywords": ["team", "help", "support"]
},
{
    "id": "hr_med_9",
    "round": "hr",
    "difficulty": "medium",
    "question": "What does workplace ethics mean to you?",
    "keywords": ["ethics", "work", "rules"]
},
{
    "id": "hr_med_10",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a challenge you overcame.",
    "keywords": ["challenge", "overcome", "problem"]
},
{
    "id": "hr_med_11",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a time when you improved a process.",
    "keywords": ["improve", "process", "change"]
},
{
    "id": "hr_med_12",
    "round": "hr",
    "difficulty": "medium",
    "question": "How do you balance work and personal life?",
    "keywords": ["balance", "work", "life"]
},
{
    "id": "hr_med_13",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe how you handle miscommunication.",
    "keywords": ["communication", "clarify", "misunderstand"]
},
{
    "id": "hr_med_14",
    "round": "hr",
    "difficulty": "medium",
    "question": "Explain your approach to long-term goals.",
    "keywords": ["goal", "long term", "plan"]
},
{
    "id": "hr_med_15",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a time you failed and what you learned.",
    "keywords": ["fail", "learn", "growth"]
},


# =========================
# HR — HARD (15)
# =========================
{
    "id": "hr_hard_1",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a major workplace dilemma and how you handled it.",
    "keywords": ["dilemma", "decision", "ethics"]
},
{
    "id": "hr_hard_2",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a situation where you had to influence someone without authority.",
    "keywords": ["influence", "persuade", "lead"]
},
{
    "id": "hr_hard_3",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe the toughest decision you’ve ever made.",
    "keywords": ["decision", "tough", "choice"]
},
{
    "id": "hr_hard_4",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when you managed a failing project.",
    "keywords": ["project", "failure", "manage"]
},
{
    "id": "hr_hard_5",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a serious conflict with a senior and how you resolved it.",
    "keywords": ["conflict", "senior", "resolve"]
},
{
    "id": "hr_hard_6",
    "round": "hr",
    "difficulty": "hard",
    "question": "Tell me about a time you had to deliver bad news.",
    "keywords": ["bad news", "communicate", "deal"]
},
{
    "id": "hr_hard_7",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain how you lead a team through a crisis.",
    "keywords": ["crisis", "lead", "team"]
},
{
    "id": "hr_hard_8",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a situation requiring extreme attention to detail.",
    "keywords": ["detail", "accuracy", "precision"]
},
{
    "id": "hr_hard_9",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when you disagreed with a company policy.",
    "keywords": ["policy", "disagree", "resolve"]
},
{
    "id": "hr_hard_10",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a time when you mentored someone through a difficult problem.",
    "keywords": ["mentor", "guide", "support"]
},
{
    "id": "hr_hard_11",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain how you handle long-term workplace burnout.",
    "keywords": ["burnout", "stress", "manage"]
},
{
    "id": "hr_hard_12",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe your approach to resolving ethical conflicts.",
    "keywords": ["ethical", "conflict", "resolve"]
},
{
    "id": "hr_hard_13",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when your leadership skills were truly tested.",
    "keywords": ["leadership", "tested", "challenge"]
},
{
    "id": "hr_hard_14",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe how you handled a major communication breakdown.",
    "keywords": ["communication", "breakdown", "fix"]
},
{
    "id": "hr_hard_15",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a time you had to make a decision that was unpopular but necessary.",
    "keywords": ["decision", "unpopular", "necessary"]
},

]


# ---------------------------------------------------
# CLEAN TEXT
# ---------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return words


# ---------------------------------------------------
# SENTIMENT ANALYSIS
# ---------------------------------------------------
def get_sentiment_score(text):
    score = sia.polarity_scores(text)
    return score["compound"]


# ---------------------------------------------------
# KEYWORD MATCHING
# ---------------------------------------------------
def keyword_score(answer, required_keywords):
    words = clean_text(answer)
    matched = sum(1 for kw in required_keywords if kw.lower() in words)

    if len(required_keywords) == 0:
        return 0

    return round((matched / len(required_keywords)) * 10, 2)


# ---------------------------------------------------
# FINAL FEEDBACK GENERATOR
# ---------------------------------------------------
def generate_feedback(question, answer, required_keywords):
    kscore = keyword_score(answer, required_keywords)
    sscore = get_sentiment_score(answer)

    feedback = []
    feedback.append(f"Keyword Score: {kscore}/10")
    feedback.append(f"Confidence Score: {round((sscore + 1) * 5, 2)}/10")

    if kscore < 5:
        feedback.append("Try including more technical keywords in your answer.")
    else:
        feedback.append("Good explanation with the right keywords.")

    if sscore < 0:
        feedback.append("Your answer could show more confidence.")
    else:
        feedback.append("Your tone reflects confidence.")

    return {
        "keyword_score": kscore,
        "sentiment_score": sscore,
        "final_feedback": " | ".join(feedback)
    }


# ---------------------------------------------------
# RANDOM QUESTION
# ---------------------------------------------------
def get_random_question():
    return random.choice(QUESTION_BANK)


# ---------------------------------------------------
# COMPANY FILTER (ROUND + DIFFICULTY)
# ---------------------------------------------------
def get_filtered_question(company, round_type, difficulty):
    """
    Filters only by round and difficulty because QUESTION_BANK
    does not contain company information.
    """

    # Ensure lowercase comparison (prevents mismatch issues)
    round_type = round_type.lower()
    difficulty = difficulty.lower()

    options = [
        q for q in QUESTION_BANK
        if q["round"].lower() == round_type
        and q["difficulty"].lower() == difficulty
    ]

    if not options:
        return None

    return random.choice(options)



# ---------------------------------------------------
# GET QUESTION BY ID
# ---------------------------------------------------
def get_question_by_id(q_id):
    for q in QUESTION_BANK:
        if q["id"] == q_id:
            return q
    return None
