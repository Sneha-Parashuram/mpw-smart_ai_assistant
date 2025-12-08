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
# 90 QUESTION DATASET (NO CHANGES MADE)
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
    "keywords": ["variable", "store", "data"],
    "answer": "A variable is a named storage location used to hold data in a program."
},
{
    "id": "tech_easy_2",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a function in programming?",
    "keywords": ["function", "reuse", "code"],
    "answer": "A function is a reusable block of code designed to perform a specific task."
},
{
    "id": "tech_easy_3",
    "round": "technical",
    "difficulty": "easy",
    "question": "Explain the purpose of loops.",
    "keywords": ["loop", "repeat", "iteration"],
    "answer": "Loops allow a program to repeat a block of code multiple times until a condition is met."
},
{
    "id": "tech_easy_4",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an array?",
    "keywords": ["array", "collection", "index"],
    "answer": "An array is a collection of elements stored at contiguous memory locations and accessed by index."
},
{
    "id": "tech_easy_5",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is debugging?",
    "keywords": ["debug", "error", "fix"],
    "answer": "Debugging is the process of identifying and fixing errors in a program."
},
{
    "id": "tech_easy_6",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an algorithm?",
    "keywords": ["algorithm", "steps", "solve"],
    "answer": "An algorithm is a step-by-step procedure used to solve a problem."
},
{
    "id": "tech_easy_7",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a data type?",
    "keywords": ["data", "type", "value"],
    "answer": "A data type defines the kind of value a variable can store, such as int, float, or string."
},
{
    "id": "tech_easy_8",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a compiler?",
    "keywords": ["compiler", "convert", "code"],
    "answer": "A compiler converts high-level source code into machine code that a computer can execute."
},
{
    "id": "tech_easy_9",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a boolean value?",
    "keywords": ["boolean", "true", "false"],
    "answer": "A boolean value represents truth values: either true or false."
},
{
    "id": "tech_easy_10",
    "round": "technical",
    "difficulty": "easy",
    "question": "What does HTML stand for?",
    "keywords": ["html", "markup", "web"],
    "answer": "HTML stands for HyperText Markup Language and is used to structure web content."
},
{
    "id": "tech_easy_11",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is CSS used for?",
    "keywords": ["css", "style", "design"],
    "answer": "CSS is used to style and design web pages, controlling layout, colors, and fonts."
},
{
    "id": "tech_easy_12",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is Git?",
    "keywords": ["git", "version", "control"],
    "answer": "Git is a version control system used to track changes and manage code efficiently."
},
{
    "id": "tech_easy_13",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is an IDE?",
    "keywords": ["ide", "environment", "code"],
    "answer": "An IDE is software that provides tools like code editors and debuggers to help developers write programs."
},
{
    "id": "tech_easy_14",
    "round": "technical",
    "difficulty": "easy",
    "question": "Define a class in OOP.",
    "keywords": ["class", "oop", "blueprint"],
    "answer": "A class in OOP is a blueprint for creating objects that share properties and behaviors."
},
{
    "id": "tech_easy_15",
    "round": "technical",
    "difficulty": "easy",
    "question": "What is a database?",
    "keywords": ["database", "store", "records"],
    "answer": "A database is an organized collection of data stored for efficient access and management."
},

# =========================
# TECHNICAL — MEDIUM (15)
# =========================
{
    "id": "tech_med_1",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain the concept of recursion.",
    "keywords": ["recursion", "function", "call"],
    "answer": "Recursion is when a function calls itself to solve a smaller version of the same problem."
},
{
    "id": "tech_med_2",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is polymorphism in OOP?",
    "keywords": ["oop", "polymorphism", "override"],
    "answer": "Polymorphism allows objects to behave differently based on which method is being invoked."
},
{
    "id": "tech_med_3",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is a REST API?",
    "keywords": ["rest", "api", "http"],
    "answer": "A REST API allows systems to communicate over HTTP using standard operations like GET and POST."
},
{
    "id": "tech_med_4",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain multithreading.",
    "keywords": ["thread", "parallel", "concurrency"],
    "answer": "Multithreading allows multiple parts of a program to run simultaneously, improving performance."
},
{
    "id": "tech_med_5",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is SQL indexing?",
    "keywords": ["index", "query", "optimize"],
    "answer": "SQL indexing speeds up data retrieval by creating a quick lookup reference for database queries."
},
{
    "id": "tech_med_6",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is memory management?",
    "keywords": ["memory", "allocate", "free"],
    "answer": "Memory management handles allocation and deallocation of memory during program execution."
},
{
    "id": "tech_med_7",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain inheritance in OOP.",
    "keywords": ["inheritance", "class", "extend"],
    "answer": "Inheritance allows one class to extend another, reusing and enhancing existing features."
},
{
    "id": "tech_med_8",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is exception handling?",
    "keywords": ["exception", "try", "catch"],
    "answer": "Exception handling manages errors gracefully using try, catch, and related mechanisms."
},
{
    "id": "tech_med_9",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain how hashing works.",
    "keywords": ["hash", "collision", "map"],
    "answer": "Hashing maps data to a fixed-size value using a hash function, enabling quick lookup operations."
},
{
    "id": "tech_med_10",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is a binary tree?",
    "keywords": ["tree", "node", "binary"],
    "answer": "A binary tree is a hierarchical structure where each node has at most two children."
},
{
    "id": "tech_med_11",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is Docker used for?",
    "keywords": ["docker", "container", "deploy"],
    "answer": "Docker is used to create, run, and manage applications inside lightweight containers."
},
{
    "id": "tech_med_12",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain DNS and its purpose.",
    "keywords": ["dns", "domain", "resolve"],
    "answer": "DNS translates human-readable domain names into IP addresses to locate websites."
},
{
    "id": "tech_med_13",
    "round": "technical",
    "difficulty": "medium",
    "question": "What is virtual memory?",
    "keywords": ["virtual", "memory", "swap"],
    "answer": "Virtual memory extends physical memory using disk space, allowing larger programs to run."
},
{
    "id": "tech_med_14",
    "round": "technical",
    "difficulty": "medium",
    "question": "Explain API authentication.",
    "keywords": ["auth", "token", "secure"],
    "answer": "API authentication verifies user identity using tokens, keys, or credentials before granting access."
},
{
    "id": "tech_med_15",
    "round": "technical",
    "difficulty": "medium",
    "question": "Describe microservices architecture.",
    "keywords": ["microservices", "distributed", "services"],
    "answer": "Microservices architecture splits applications into small, independent services that work together."
},

# =========================
# TECHNICAL — HARD (15)
# =========================
{
    "id": "tech_hard_1",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain how operating systems handle deadlocks.",
    "keywords": ["deadlock", "os", "resource"],
    "answer": "Operating systems handle deadlocks through prevention, avoidance, detection, and recovery techniques."
},
{
    "id": "tech_hard_2",
    "round": "technical",
    "difficulty": "hard",
    "question": "What is ACID compliance in databases?",
    "keywords": ["acid", "transaction", "consistency"],
    "answer": "ACID compliance ensures database transactions are reliable through atomicity, consistency, isolation, and durability."
},
{
    "id": "tech_hard_3",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain time and space complexity of algorithms.",
    "keywords": ["complexity", "big o", "analysis"],
    "answer": "Time and space complexity measure how an algorithm’s performance scales with input size."
},
{
    "id": "tech_hard_4",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe load balancing algorithms.",
    "keywords": ["load", "balance", "algorithm"],
    "answer": "Load balancing distributes traffic across servers to improve performance and reduce overload."
},
{
    "id": "tech_hard_5",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain distributed system consistency models.",
    "keywords": ["distributed", "consistency", "model"],
    "answer": "Consistency models define how distributed systems ensure data correctness across nodes."
},
{
    "id": "tech_hard_6",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain the CAP theorem.",
    "keywords": ["cap", "consistency", "availability"],
    "answer": "The CAP theorem states that a distributed system can only guarantee two of consistency, availability, and partition tolerance."
},
{
    "id": "tech_hard_7",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain how garbage collection works.",
    "keywords": ["garbage", "memory", "collector"],
    "answer": "Garbage collection automatically frees unused memory by detecting unreachable objects."
},
{
    "id": "tech_hard_8",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how a compiler optimizes code during compilation.",
    "keywords": ["compiler", "optimize", "code"],
    "answer": "Compilers optimize code by improving execution speed or reducing size during compilation."
},
{
    "id": "tech_hard_9",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain database sharding and replication.",
    "keywords": ["shard", "replica", "scale"],
    "answer": "Database sharding splits data across servers, while replication copies data for reliability."
},
{
    "id": "tech_hard_10",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how neural networks learn during training.",
    "keywords": ["neural", "train", "weights"],
    "answer": "Neural networks learn by adjusting weights using training data and backpropagation."
},
{
    "id": "tech_hard_11",
    "round": "technical",
    "difficulty": "hard",
    "question": "What is a race condition and how can it be prevented?",
    "keywords": ["race", "thread", "lock"],
    "answer": "A race condition occurs when threads access shared data simultaneously and can be prevented using locks."
},
{
    "id": "tech_hard_12",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe how a blockchain maintains trust.",
    "keywords": ["blockchain", "hash", "trust"],
    "answer": "A blockchain maintains trust using cryptographic hashing and decentralized consensus."
},
{
    "id": "tech_hard_13",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain network congestion control algorithms.",
    "keywords": ["network", "congestion", "algorithm"],
    "answer": "Congestion control algorithms manage network traffic to avoid overload and maintain performance."
},
{
    "id": "tech_hard_14",
    "round": "technical",
    "difficulty": "hard",
    "question": "Explain the internals of a virtual machine hypervisor.",
    "keywords": ["hypervisor", "vm", "virtual"],
    "answer": "A hypervisor manages virtual machines by allocating resources and isolating environments."
},
{
    "id": "tech_hard_15",
    "round": "technical",
    "difficulty": "hard",
    "question": "Describe Paxos or Raft consensus algorithm.",
    "keywords": ["consensus", "raft", "paxos"],
    "answer": "Paxos and Raft ensure distributed nodes reach consensus even when some fail."
},
# =========================
# HR — EASY (15)
# =========================
{
    "id": "hr_easy_1",
    "round": "hr",
    "difficulty": "easy",
    "question": "Tell me about yourself.",
    "keywords": ["intro", "background", "yourself"],
    "answer": "I am a motivated individual with a strong interest in learning and growth, and I have experience in both academics and team projects."
},
{
    "id": "hr_easy_2",
    "round": "hr",
    "difficulty": "easy",
    "question": "Why do you want this job?",
    "keywords": ["job", "reason", "motivation"],
    "answer": "I want this job because it aligns with my skills and offers opportunities for growth while contributing to meaningful work."
},
{
    "id": "hr_easy_3",
    "round": "hr",
    "difficulty": "easy",
    "question": "What are your strengths?",
    "keywords": ["strength", "skill", "ability"],
    "answer": "My strengths include problem-solving, quick learning, and the ability to work well in a team."
},
{
    "id": "hr_easy_4",
    "round": "hr",
    "difficulty": "easy",
    "question": "Describe your weakness.",
    "keywords": ["weakness", "improve", "challenge"],
    "answer": "One weakness is over-focusing on details, but I am improving by prioritizing tasks effectively."
},
{
    "id": "hr_easy_5",
    "round": "hr",
    "difficulty": "easy",
    "question": "Where do you see yourself in five years?",
    "keywords": ["future", "plan", "career"],
    "answer": "In five years, I see myself growing into a more responsible role while contributing significantly to my team."
},
{
    "id": "hr_easy_6",
    "round": "hr",
    "difficulty": "easy",
    "question": "What motivates you?",
    "keywords": ["motivate", "drive", "goal"],
    "answer": "I am motivated by learning new things, achieving goals, and seeing the impact of my work."
},
{
    "id": "hr_easy_7",
    "round": "hr",
    "difficulty": "easy",
    "question": "Describe a time you worked in a team.",
    "keywords": ["team", "collaboration", "work"],
    "answer": "I worked in a team during a college project where we collaborated to divide tasks and successfully complete the assignment."
},
{
    "id": "hr_easy_8",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you handle stress?",
    "keywords": ["stress", "handle", "pressure"],
    "answer": "I handle stress by staying organized, focusing on one task at a time, and keeping a positive mindset."
},
{
    "id": "hr_easy_9",
    "round": "hr",
    "difficulty": "easy",
    "question": "What do you know about our company?",
    "keywords": ["company", "research", "info"],
    "answer": "Your company is known for innovation, strong work culture, and creating impactful solutions in the industry."
},
{
    "id": "hr_easy_10",
    "round": "hr",
    "difficulty": "easy",
    "question": "What hobbies do you have?",
    "keywords": ["hobby", "interest", "activity"],
    "answer": "My hobbies include reading, learning new skills, and participating in creative or technical activities."
},
{
    "id": "hr_easy_11",
    "round": "hr",
    "difficulty": "easy",
    "question": "Do you consider yourself a leader?",
    "keywords": ["leader", "leadership", "team"],
    "answer": "Yes, I believe I show leadership by taking initiative, guiding others, and helping the team stay on track."
},
{
    "id": "hr_easy_12",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you stay organized?",
    "keywords": ["organized", "plan", "task"],
    "answer": "I stay organized by planning tasks ahead, maintaining to-do lists, and managing my time effectively."
},
{
    "id": "hr_easy_13",
    "round": "hr",
    "difficulty": "easy",
    "question": "Tell me about a small achievement you are proud of.",
    "keywords": ["achievement", "proud", "goal"],
    "answer": "I am proud of improving my technical skills by completing projects that challenged me to learn new concepts."
},
{
    "id": "hr_easy_14",
    "round": "hr",
    "difficulty": "easy",
    "question": "How do you adapt to new situations?",
    "keywords": ["adapt", "change", "flexible"],
    "answer": "I adapt quickly by staying flexible, observing the environment, and adjusting my approach when needed."
},
{
    "id": "hr_easy_15",
    "round": "hr",
    "difficulty": "easy",
    "question": "Do you prefer working alone or in a team?",
    "keywords": ["team", "alone", "work"],
    "answer": "I am comfortable with both, but I enjoy teamwork because it encourages learning and diverse ideas."
},


# =========================
# HR — MEDIUM (15)
# =========================
{
    "id": "hr_med_1",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a conflict you resolved at work or college.",
    "keywords": ["conflict", "resolve", "problem"],
    "answer": "I resolved a conflict during a group project by listening to both sides and helping the team agree on a fair plan."
},
{
    "id": "hr_med_2",
    "round": "hr",
    "difficulty": "medium",
    "question": "Explain how you respond to negative feedback.",
    "keywords": ["feedback", "improve", "response"],
    "answer": "I take negative feedback positively, reflect on it, and use it to improve my skills or behavior."
},
{
    "id": "hr_med_3",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a time you showed leadership.",
    "keywords": ["leadership", "team", "initiative"],
    "answer": "I showed leadership by organizing my team, assigning roles, and ensuring everyone contributed effectively."
},
{
    "id": "hr_med_4",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe your decision-making process.",
    "keywords": ["decision", "process", "choice"],
    "answer": "I make decisions by analyzing options, considering risks, and choosing the solution that best fits the goal."
},
{
    "id": "hr_med_5",
    "round": "hr",
    "difficulty": "medium",
    "question": "What motivates you to perform well?",
    "keywords": ["motivate", "performance", "drive"],
    "answer": "I am motivated by challenging work, achieving measurable results, and growing professionally."
},
{
    "id": "hr_med_6",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a risk you took and what happened.",
    "keywords": ["risk", "decision", "outcome"],
    "answer": "I once took a risk by volunteering for a complex task, and completing it successfully boosted my confidence."
},
{
    "id": "hr_med_7",
    "round": "hr",
    "difficulty": "medium",
    "question": "How do you manage tight deadlines?",
    "keywords": ["deadline", "time", "stress"],
    "answer": "I manage tight deadlines by prioritizing the most important tasks and staying focused on efficient execution."
},
{
    "id": "hr_med_8",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a time you helped a struggling teammate.",
    "keywords": ["team", "help", "support"],
    "answer": "I once supported a teammate by explaining concepts they found difficult and helping them finish their tasks."
},
{
    "id": "hr_med_9",
    "round": "hr",
    "difficulty": "medium",
    "question": "What does workplace ethics mean to you?",
    "keywords": ["ethics", "work", "rules"],
    "answer": "Workplace ethics means doing the right thing consistently, maintaining honesty, and respecting others."
},
{
    "id": "hr_med_10",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a challenge you overcame.",
    "keywords": ["challenge", "overcome", "problem"],
    "answer": "I overcame a challenge by setting small goals, staying determined, and seeking guidance when needed."
},
{
    "id": "hr_med_11",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe a time when you improved a process.",
    "keywords": ["improve", "process", "change"],
    "answer": "I improved a process by suggesting a more efficient workflow that saved time for the entire team."
},
{
    "id": "hr_med_12",
    "round": "hr",
    "difficulty": "medium",
    "question": "How do you balance work and personal life?",
    "keywords": ["balance", "work", "life"],
    "answer": "I balance work and personal life by planning ahead and making time for rest and family."
},
{
    "id": "hr_med_13",
    "round": "hr",
    "difficulty": "medium",
    "question": "Describe how you handle miscommunication.",
    "keywords": ["communication", "clarify", "misunderstand"],
    "answer": "I handle miscommunication by clarifying doubts, confirming details, and keeping communication open."
},
{
    "id": "hr_med_14",
    "round": "hr",
    "difficulty": "medium",
    "question": "Explain your approach to long-term goals.",
    "keywords": ["goal", "long term", "plan"],
    "answer": "I set long-term goals by breaking them into smaller steps and reviewing my progress regularly."
},
{
    "id": "hr_med_15",
    "round": "hr",
    "difficulty": "medium",
    "question": "Tell me about a time you failed and what you learned.",
    "keywords": ["fail", "learn", "growth"],
    "answer": "I once failed at a task, but I learned to prepare better and not hesitate to ask for help."
},


# =========================
# HR — HARD (15)
# =========================
{
    "id": "hr_hard_1",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a major workplace dilemma and how you handled it.",
    "keywords": ["dilemma", "decision", "ethics"],
    "answer": "I handled a workplace dilemma by evaluating the ethical concerns and choosing the option that maintained fairness."
},
{
    "id": "hr_hard_2",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a situation where you had to influence someone without authority.",
    "keywords": ["influence", "persuade", "lead"],
    "answer": "I influenced a teammate by presenting logical reasons, showing benefits, and earning their trust."
},
{
    "id": "hr_hard_3",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe the toughest decision you’ve ever made.",
    "keywords": ["decision", "tough", "choice"],
    "answer": "One of my toughest decisions was choosing between two important priorities, and I made it by evaluating long-term impact."
},
{
    "id": "hr_hard_4",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when you managed a failing project.",
    "keywords": ["project", "failure", "manage"],
    "answer": "I managed a failing project by identifying issues early, reorganizing tasks, and motivating the team to stay on track."
},
{
    "id": "hr_hard_5",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a serious conflict with a senior and how you resolved it.",
    "keywords": ["conflict", "senior", "resolve"],
    "answer": "I resolved a conflict with a senior by communicating respectfully and finding a solution that worked for both of us."
},
{
    "id": "hr_hard_6",
    "round": "hr",
    "difficulty": "hard",
    "question": "Tell me about a time you had to deliver bad news.",
    "keywords": ["bad news", "communicate", "deal"],
    "answer": "I delivered bad news by staying honest, explaining the situation clearly, and offering support where possible."
},
{
    "id": "hr_hard_7",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain how you lead a team through a crisis.",
    "keywords": ["crisis", "lead", "team"],
    "answer": "I led a team through a crisis by staying calm, assigning clear tasks, and keeping everyone motivated."
},
{
    "id": "hr_hard_8",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a situation requiring extreme attention to detail.",
    "keywords": ["detail", "accuracy", "precision"],
    "answer": "I handled a high-precision task by double-checking data and ensuring every step met the required accuracy."
},
{
    "id": "hr_hard_9",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when you disagreed with a company policy.",
    "keywords": ["policy", "disagree", "resolve"],
    "answer": "I disagreed with a policy but shared my concerns politely and worked with the team to propose improvements."
},
{
    "id": "hr_hard_10",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a time when you mentored someone through a difficult problem.",
    "keywords": ["mentor", "guide", "support"],
    "answer": "I mentored a junior teammate by breaking down the problem and guiding them step-by-step until they understood it."
},
{
    "id": "hr_hard_11",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain how you handle long-term workplace burnout.",
    "keywords": ["burnout", "stress", "manage"],
    "answer": "I manage burnout by taking breaks, setting boundaries, and focusing on activities that help me recharge."
},
{
    "id": "hr_hard_12",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe your approach to resolving ethical conflicts.",
    "keywords": ["ethical", "conflict", "resolve"],
    "answer": "I resolve ethical conflicts by prioritizing honesty, fairness, and long-term integrity."
},
{
    "id": "hr_hard_13",
    "round": "hr",
    "difficulty": "hard",
    "question": "Explain a time when your leadership skills were truly tested.",
    "keywords": ["leadership", "tested", "challenge"],
    "answer": "My leadership was tested when my team faced setbacks, and I motivated them while coordinating a recovery plan."
},
{
    "id": "hr_hard_14",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe how you handled a major communication breakdown.",
    "keywords": ["communication", "breakdown", "fix"],
    "answer": "I handled a communication breakdown by clearing misunderstandings, re-establishing expectations, and improving communication flow."
},
{
    "id": "hr_hard_15",
    "round": "hr",
    "difficulty": "hard",
    "question": "Describe a time you had to make a decision that was unpopular but necessary.",
    "keywords": ["decision", "unpopular", "necessary"],
    "answer": "I made an unpopular decision because it was necessary for long-term success, and I communicated the reasoning clearly."
},

]

# ---------------------------------------------------
# TEXT CLEANING
# ---------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = "".join(c for c in text if c not in string.punctuation)
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return words


# ---------------------------------------------------
# SENTIMENT (float only)
# ---------------------------------------------------
def get_sentiment_score(text):
    try:
        return float(sia.polarity_scores(text)["compound"])
    except Exception:
        return 0.0


# ---------------------------------------------------
# FIXED KEYWORD MATCHING (float only — NEVER tuple)
# ---------------------------------------------------
def calculate_keyword_score(answer, required_keywords):
    """
    SAFE VERSION — returns:
        keyword_score: float
        matched_keywords: list
    """

    answer = answer.lower()
    matched = [kw for kw in required_keywords if kw.lower() in answer]

    if not required_keywords:
        return 0.0, []

    score = round((len(matched) / len(required_keywords)) * 5, 2)
    return float(score), matched


# ---------------------------------------------------
# FINAL FEEDBACK GENERATOR — FULLY FIXED
# ---------------------------------------------------
def generate_feedback(question, answer, required_keywords, actual_answer=""):
    """
    FINAL version (DB-safe):
    RETURNS:
        keyword_score: float
        sentiment_score: float
        final_feedback: string
    """

    # -------------------------
    # 1. Keyword Scoring
    # -------------------------
    keyword_score, matched = calculate_keyword_score(answer, required_keywords)

    # -------------------------
    # 2. Sentiment Score
    # -------------------------
    sentiment_score = get_sentiment_score(answer)

    # -------------------------
    # 3. Build Feedback Text
    # -------------------------
    fb = []

    if actual_answer:
        fb.append(f"Actual Answer: {actual_answer}")

    fb.append(f"Your Answer: {answer}")
    fb.append(f"Keywords Found: {', '.join(matched) if matched else 'None'}")
    fb.append(f"Keyword Score: {keyword_score}/5")

    if sentiment_score > 0.2:
        fb.append("Tone: Positive and confident.")
    elif sentiment_score < -0.2:
        fb.append("Tone: Needs more clarity or confidence.")
    else:
        fb.append("Tone: Neutral and balanced.")

    final_feedback = " | ".join(fb)

    # -------------------------
    # 4. RETURN FOR DATABASE
    # -------------------------
    return {
        "keyword_score": float(keyword_score),
        "sentiment_score": float(sentiment_score),
        "final_feedback": final_feedback
    }


# ---------------------------------------------------
# RANDOM QUESTION
# ---------------------------------------------------
def get_random_question():
    return random.choice(QUESTION_BANK)


# ---------------------------------------------------
# FILTER QUESTION
# ---------------------------------------------------
def get_filtered_question(company, round_type, difficulty):
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
