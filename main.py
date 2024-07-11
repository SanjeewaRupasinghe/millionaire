import time
from tkinter import *
from random import randint
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

# VARIABLES
global idValue, questionArea
lang = 'en'
selectedIds = []
questionArray = []


# CHANGE questionArray BY CHECKING lang VARIABLE
def languageCheck():
    global questionArray
    if lang == "en":
        questionArray = [
            {
                "question": "What is the main ingredient in traditional paella?",
                "a": "Rice",
                "b": "Potato",
                "c": "Pasta",
                "d": "Bread",
                "correct": "Rice",
                "speak": "Rice"
            },
            {
                "question": "Which planet is closest to the sun?",
                "a": "Venus",
                "b": "Mars",
                "c": "Mercury",
                "d": "Earth",
                "correct": "Mercury",
                "speak": "Mercury"
            },
            {
                "question": "What is the largest desert in the world?",
                "a": "Sahara Desert",
                "b": "Arabian Desert",
                "c": "Gobi Desert",
                "d": "Kalahari Desert",
                "correct": "Sahara Desert",
                "speak": "Sahara Desert"
            },
            {
                "question": "Who painted the 'Starry Night'?",
                "a": "Pablo Picasso",
                "b": "Leonardo da Vinci",
                "c": "Vincent van Gogh",
                "d": "Claude Monet",
                "correct": "Vincent van Gogh",
                "speak": "Vincent van Gogh"
            },
            {
                "question": "What is the smallest bone in the human body?",
                "a": "Stapes",
                "b": "Femur",
                "c": "Tibia",
                "d": "Fibula",
                "correct": "Stapes",
                "speak": "Stapes"
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "a": "Harper Lee",
                "b": "Mark Twain",
                "c": "F. Scott Fitzgerald",
                "d": "Ernest Hemingway",
                "correct": "Harper Lee",
                "speak": "Harper Lee"
            },
            {
                "question": "What is the chemical symbol for sodium?",
                "a": "Na",
                "b": "So",
                "c": "Sa",
                "d": "N",
                "correct": "Na",
                "speak": "N A"
            },
            {
                "question": "Who developed the theory of relativity?",
                "a": "Isaac Newton",
                "b": "Galileo Galilei",
                "c": "Albert Einstein",
                "d": "Niels Bohr",
                "correct": "Albert Einstein",
                "speak": "Albert Einstein"
            },
            {
                "question": "Which planet is known as the 'Blue Planet'?",
                "a": "Mars",
                "b": "Earth",
                "c": "Neptune",
                "d": "Uranus",
                "correct": "Earth",
                "speak": "Earth"
            },
            {
                "question": "What is the tallest building in the world?",
                "a": "Shanghai Tower",
                "b": "Abraj Al-Bait",
                "c": "Burj Khalifa",
                "d": "One World Trade Center",
                "correct": "Burj Khalifa",
                "speak": "Burj Khalifa"
            },
            {
                "question": "What is the currency of Japan?",
                "a": "Yuan",
                "b": "Won",
                "c": "Yen",
                "d": "Dollar",
                "correct": "Yen",
                "speak": "Yen"
            },
            {
                "question": "Who invented the telephone?",
                "a": "Thomas Edison",
                "b": "Nikola Tesla",
                "c": "Alexander Graham Bell",
                "d": "Guglielmo Marconi",
                "correct": "Alexander Graham Bell",
                "speak": "Alexander Graham Bell"
            },
            {
                "question": "What is the smallest country in the world?",
                "a": "Monaco",
                "b": "San Marino",
                "c": "Vatican City",
                "d": "Liechtenstein",
                "correct": "Vatican City",
                "speak": "Vatican City"
            },
            {
                "question": "Which ocean is the largest?",
                "a": "Atlantic Ocean",
                "b": "Indian Ocean",
                "c": "Arctic Ocean",
                "d": "Pacific Ocean",
                "correct": "Pacific Ocean",
                "speak": "Pacific Ocean"
            },
            {
                "question": "What is the largest island in the world?",
                "a": "Greenland",
                "b": "New Guinea",
                "c": "Borneo",
                "d": "Madagascar",
                "correct": "Greenland",
                "speak": "Greenland"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "a": "Leonardo da Vinci",
                "b": "Vincent van Gogh",
                "c": "Pablo Picasso",
                "d": "Claude Monet",
                "correct": "Leonardo da Vinci",
                "speak": "Leonardo da Vinci"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "a": "Atlantic Ocean",
                "b": "Indian Ocean",
                "c": "Southern Ocean",
                "d": "Pacific Ocean",
                "correct": "Pacific Ocean",
                "speak": "Pacific Ocean"
            },
            {
                "question": "Who wrote 'Pride and Prejudice'?",
                "a": "Jane Austen",
                "b": "Charlotte Bronte",
                "c": "Emily Bronte",
                "d": "George Eliot",
                "correct": "Jane Austen",
                "speak": "Jane Austen"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "a": "K2",
                "b": "Mount Everest",
                "c": "Kangchenjunga",
                "d": "Lhotse",
                "correct": "Mount Everest",
                "speak": "Mount Everest"
            },
            {
                "question": "What is the smallest planet in our solar system?",
                "a": "Mars",
                "b": "Venus",
                "c": "Mercury",
                "d": "Pluto",
                "correct": "Mercury",
                "speak": "Mercury"
            },
            {
                "question": "What is the largest continent?",
                "a": "Africa",
                "b": "Asia",
                "c": "Europe",
                "d": "North America",
                "correct": "Asia",
                "speak": "Asia"
            },
            {
                "question": "Who developed the polio vaccine?",
                "a": "Albert Sabin",
                "b": "Louis Pasteur",
                "c": "Alexander Fleming",
                "d": "Jonas Salk",
                "correct": "Jonas Salk",
                "speak": "Jonas Salk"
            },
            {
                "question": "What is the primary language spoken in Brazil?",
                "a": "Spanish",
                "b": "Portuguese",
                "c": "English",
                "d": "French",
                "correct": "Portuguese",
                "speak": "Portuguese"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "a": "Osmium",
                "b": "Oxygen",
                "c": "Oganesson",
                "d": "Oxalate",
                "correct": "Oxygen",
                "speak": "Oxygen"
            },
            {
                "question": "Which famous ship sank in 1912?",
                "a": "Lusitania",
                "b": "Britannic",
                "c": "Titanic",
                "d": "Queen Mary",
                "correct": "Titanic",
                "speak": "Titanic"
            },
            {
                "question": "What is the largest mammal in the world?",
                "a": "African Elephant",
                "b": "Blue Whale",
                "c": "Giraffe",
                "d": "Great White Shark",
                "correct": "Blue Whale",
                "speak": "Blue Whale"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "a": "Charles Dickens",
                "b": "Jane Austen",
                "c": "William Shakespeare",
                "d": "Mark Twain",
                "correct": "William Shakespeare",
                "speak": "William Shakespeare"
            },
            {
                "question": "What is the main component of the sun?",
                "a": "Oxygen",
                "b": "Hydrogen",
                "c": "Carbon",
                "d": "Helium",
                "correct": "Hydrogen",
                "speak": "Hydrogen"
            },
            {
                "question": "What is the capital of China?",
                "a": "Shanghai",
                "b": "Beijing",
                "c": "Hong Kong",
                "d": "Chengdu",
                "correct": "Beijing",
                "speak": "Beijing"
            },
            {
                "question": "What is the primary gas found in the Earth's atmosphere?",
                "a": "Oxygen",
                "b": "Carbon Dioxide",
                "c": "Nitrogen",
                "d": "Hydrogen",
                "correct": "Nitrogen",
                "speak": "Nitrogen"
            },
            {
                "question": "Who painted the ceiling of the Sistine Chapel?",
                "a": "Leonardo da Vinci",
                "b": "Raphael",
                "c": "Michelangelo",
                "d": "Donatello",
                "correct": "Michelangelo",
                "speak": "Michelangelo"
            },
            {
                "question": "What is the tallest animal in the world?",
                "a": "Elephant",
                "b": "Blue Whale",
                "c": "Giraffe",
                "d": "Great White Shark",
                "correct": "Giraffe",
                "speak": "Giraffe"
            },
            {
                "question": "What is the most spoken language in the world?",
                "a": "Spanish",
                "b": "English",
                "c": "Mandarin",
                "d": "Hindi",
                "correct": "Mandarin",
                "speak": "Mandarin"
            },
            {
                "question": "What is the currency of India?",
                "a": "Rupee",
                "b": "Taka",
                "c": "Rial",
                "d": "Yen",
                "correct": "Rupee",
                "speak": "Rupee"
            },
            {
                "question": "What is the tallest waterfall in the world?",
                "a": "Niagara Falls",
                "b": "Angel Falls",
                "c": "Victoria Falls",
                "d": "Iguazu Falls",
                "correct": "Angel Falls",
                "speak": "Angel Falls"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "a": "Jupiter",
                "b": "Mars",
                "c": "Saturn",
                "d": "Neptune",
                "correct": "Mars",
                "speak": "Mars"
            },
            {
                "question": "Who wrote 'The Divine Comedy'?",
                "a": "Dante Alighieri",
                "b": "Geoffrey Chaucer",
                "c": "William Blake",
                "d": "John Milton",
                "correct": "Dante Alighieri",
                "speak": "Dante Alighieri"
            },
            {
                "question": "What is the capital of Germany?",
                "a": "Munich",
                "b": "Frankfurt",
                "c": "Berlin",
                "d": "Hamburg",
                "correct": "Berlin",
                "speak": "Berlin"
            },
            {
                "question": "Who is the author of 'The Great Gatsby'?",
                "a": "Ernest Hemingway",
                "b": "J.D. Salinger",
                "c": "F. Scott Fitzgerald",
                "d": "John Steinbeck",
                "correct": "F. Scott Fitzgerald",
                "speak": "F. Scott Fitzgerald"
            },
            {
                "question": "What is the currency of China?",
                "a": "Yen",
                "b": "Won",
                "c": "Yuan",
                "d": "Rupee",
                "correct": "Yuan",
                "speak": "Yuan"
            },
            {
                "question": "Who is known as the father of computing?",
                "a": "Alan Turing",
                "b": "Charles Babbage",
                "c": "John von Neumann",
                "d": "Bill Gates",
                "correct": "Charles Babbage",
                "speak": "Charles Babbage"
            },
            {
                "question": "What does 'HTTP' stand for?",
                "a": "HyperText Transfer Protocol",
                "b": "HyperText Transmission Protocol",
                "c": "Hyper Transfer Text Protocol",
                "d": "Hyper Transmission Text Protocol",
                "correct": "HyperText Transfer Protocol",
                "speak": "HyperText Transfer Protocol"
            },
            {
                "question": "Who invented the World Wide Web?",
                "a": "Tim Berners-Lee",
                "b": "Bill Gates",
                "c": "Steve Jobs",
                "d": "Mark Zuckerberg",
                "correct": "Tim Berners-Lee",
                "speak": "Tim Berners-Lee"
            },
            {
                "question": "What does 'CPU' stand for in computers?",
                "a": "Central Processing Unit",
                "b": "Central Power Unit",
                "c": "Central Programming Unit",
                "d": "Central Print Unit",
                "correct": "Central Processing Unit",
                "speak": "Central Processing Unit"
            },
            {
                "question": "Which company developed the Android operating system?",
                "a": "Apple",
                "b": "Microsoft",
                "c": "Google",
                "d": "Samsung",
                "correct": "Google",
                "speak": "Google"
            },
            {
                "question": "What does 'RAM' stand for?",
                "a": "Random Access Memory",
                "b": "Read Access Memory",
                "c": "Read-Only Memory",
                "d": "Randomly Allocated Memory",
                "correct": "Random Access Memory",
                "speak": "Random Access Memory"
            },
            {
                "question": "What is the name of the first electronic general-purpose computer?",
                "a": "UNIVAC",
                "b": "ENIAC",
                "c": "EDVAC",
                "d": "IBM 701",
                "correct": "ENIAC",
                "speak": "ENIAC"
            },
            {
                "question": "What is the name of the first graphical web browser?",
                "a": "Internet Explorer",
                "b": "Netscape Navigator",
                "c": "Mosaic",
                "d": "Opera",
                "correct": "Mosaic",
                "speak": "Mosaic"
            },
            {
                "question": "What is the name of Microsoft's cloud computing service?",
                "a": "Azure",
                "b": "AWS",
                "c": "Google Cloud",
                "d": "IBM Cloud",
                "correct": "Azure",
                "speak": "Azure"
            },
            {
                "question": "Who co-founded Microsoft with Bill Gates?",
                "a": "Steve Wozniak",
                "b": "Paul Allen",
                "c": "Larry Page",
                "d": "Sergey Brin",
                "correct": "Paul Allen",
                "speak": "Paul Allen"
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "a": "Python",
                "b": "Java",
                "c": "C++",
                "d": "JavaScript",
                "correct": "JavaScript",
                "speak": "JavaScript"
            },
            {
                "question": "What does 'URL' stand for?",
                "a": "Uniform Resource Locator",
                "b": "Uniform Reference Locator",
                "c": "Universal Resource Locator",
                "d": "Universal Reference Locator",
                "correct": "Uniform Resource Locator",
                "speak": "Uniform Resource Locator"
            },
            {
                "question": "Which company is known for the 'ThinkPad' line of laptops?",
                "a": "Apple",
                "b": "HP",
                "c": "Dell",
                "d": "Lenovo",
                "correct": "Lenovo",
                "speak": "Lenovo"
            },
            {
                "question": "What does 'PDF' stand for?",
                "a": "Portable Document Format",
                "b": "Public Document Format",
                "c": "Portable Data Format",
                "d": "Public Data Format",
                "correct": "Portable Document Format",
                "speak": "Portable Document Format"
            },
            {
                "question": "Which company developed the first microprocessor?",
                "a": "Intel",
                "b": "AMD",
                "c": "IBM",
                "d": "Texas Instruments",
                "correct": "Intel",
                "speak": "Intel"
            },
            {
                "question": "What is the most popular programming language as of 2021?",
                "a": "Python",
                "b": "JavaScript",
                "c": "Java",
                "d": "C++",
                "correct": "Python",
                "speak": "Python"
            },
            {
                "question": "What year was the first version of Windows released?",
                "a": "1983",
                "b": "1984",
                "c": "1985",
                "d": "1986",
                "correct": "1985",
                "speak": "1985"
            },
            {
                "question": "What does 'SSD' stand for in computer storage?",
                "a": "Solid State Drive",
                "b": "Secure Storage Device",
                "c": "Solid Storage Drive",
                "d": "Secure State Drive",
                "correct": "Solid State Drive",
                "speak": "Solid State Drive"
            },
            {
                "question": "Which company is known for its GeForce graphics cards?",
                "a": "AMD",
                "b": "Intel",
                "c": "NVIDIA",
                "d": "ASUS",
                "correct": "NVIDIA",
                "speak": "NVIDIA"
            },
            {
                "question": "What is the name of Apple's desktop operating system?",
                "a": "iOS",
                "b": "macOS",
                "c": "Windows",
                "d": "Linux",
                "correct": "macOS",
                "speak": "macOS"
            },
            {
                "question": "Which company created the PlayStation gaming console?",
                "a": "Microsoft",
                "b": "Nintendo",
                "c": "Sony",
                "d": "Sega",
                "correct": "Sony",
                "speak": "Sony"
            },
            {
                "question": "What does 'LAN' stand for?",
                "a": "Local Area Network",
                "b": "Large Area Network",
                "c": "Long Area Network",
                "d": "Limited Area Network",
                "correct": "Local Area Network",
                "speak": "Local Area Network"
            },
            {
                "question": "Which social media platform was founded by Mark Zuckerberg?",
                "a": "Twitter",
                "b": "Instagram",
                "c": "LinkedIn",
                "d": "Facebook",
                "correct": "Facebook",
                "speak": "Facebook"
            },
            {
                "question": "Which programming language is primarily used for iOS development?",
                "a": "Java",
                "b": "Swift",
                "c": "C#",
                "d": "Ruby",
                "correct": "Swift",
                "speak": "Swift"
            },
            {
                "question": "What does 'VPN' stand for?",
                "a": "Virtual Private Network",
                "b": "Virtual Public Network",
                "c": "Virtual Protected Network",
                "d": "Virtual Personal Network",
                "correct": "Virtual Private Network",
                "speak": "Virtual Private Network"
            },
            {
                "question": "Which company developed the Linux operating system?",
                "a": "IBM",
                "b": "Microsoft",
                "c": "Red Hat",
                "d": "None of the above",
                "correct": "None of the above",
                "speak": "None of the above"
            },
            {
                "question": "What year was YouTube founded?",
                "a": "2003",
                "b": "2004",
                "c": "2005",
                "d": "2006",
                "correct": "2005",
                "speak": "2005"
            },
            {
                "question": "What does 'IoT' stand for?",
                "a": "Internet of Things",
                "b": "Internet of Technology",
                "c": "Internet of Tools",
                "d": "Internet of Transactions",
                "correct": "Internet of Things",
                "speak": "Internet of Things"
            },
            {
                "question": "Which company manufactures the Surface line of tablets?",
                "a": "Apple",
                "b": "Samsung",
                "c": "Microsoft",
                "d": "Google",
                "correct": "Microsoft",
                "speak": "Microsoft"
            },
            {
                "question": "What does 'AI' stand for?",
                "a": "Automated Intelligence",
                "b": "Artificial Intelligence",
                "c": "Actual Intelligence",
                "d": "Augmented Intelligence",
                "correct": "Artificial Intelligence",
                "speak": "Artificial Intelligence"
            },
            {
                "question": "Who is the CEO of Tesla as of 2021?",
                "a": "Jeff Bezos",
                "b": "Tim Cook",
                "c": "Elon Musk",
                "d": "Sundar Pichai",
                "correct": "Elon Musk",
                "speak": "Elon Musk"
            },
            {
                "question": "Who was the first President of the United States?",
                "a": "George Washington",
                "b": "Thomas Jefferson",
                "c": "John Adams",
                "d": "James Madison",
                "correct": "George Washington",
                "speak": "George Washington"
            },
            {
                "question": "In which year did World War II end?",
                "a": "1943",
                "b": "1944",
                "c": "1945",
                "d": "1946",
                "correct": "1945",
                "speak": "1945"
            },
            {
                "question": "Who was known as the Iron Lady?",
                "a": "Angela Merkel",
                "b": "Indira Gandhi",
                "c": "Margaret Thatcher",
                "d": "Golda Meir",
                "correct": "Margaret Thatcher",
                "speak": "Margaret Thatcher"
            },
            {
                "question": "Which empire was ruled by Alexander the Great?",
                "a": "Roman Empire",
                "b": "Macedonian Empire",
                "c": "Persian Empire",
                "d": "Ottoman Empire",
                "correct": "Macedonian Empire",
                "speak": "Macedonian Empire"
            },
            {
                "question": "Who discovered America?",
                "a": "Marco Polo",
                "b": "Ferdinand Magellan",
                "c": "Christopher Columbus",
                "d": "Vasco da Gama",
                "correct": "Christopher Columbus",
                "speak": "Christopher Columbus"
            },
            {
                "question": "In which year did the French Revolution begin?",
                "a": "1776",
                "b": "1789",
                "c": "1799",
                "d": "1804",
                "correct": "1789",
                "speak": "1789"
            },
            {
                "question": "Who was the first man to step on the Moon?",
                "a": "Buzz Aldrin",
                "b": "Yuri Gagarin",
                "c": "John Glenn",
                "d": "Neil Armstrong",
                "correct": "Neil Armstrong",
                "speak": "Neil Armstrong"
            },
            {
                "question": "Which ancient civilization built the pyramids?",
                "a": "Roman",
                "b": "Greek",
                "c": "Egyptian",
                "d": "Mayan",
                "correct": "Egyptian",
                "speak": "Egyptian"
            },
            {
                "question": "Who was the main author of the Declaration of Independence?",
                "a": "John Adams",
                "b": "Benjamin Franklin",
                "c": "Thomas Jefferson",
                "d": "James Madison",
                "correct": "Thomas Jefferson",
                "speak": "Thomas Jefferson"
            },
            {
                "question": "What was the primary cause of the American Civil War?",
                "a": "Economic differences",
                "b": "Slavery",
                "c": "Territorial expansion",
                "d": "Political parties",
                "correct": "Slavery",
                "speak": "Slavery"
            },
            {
                "question": "Who was the longest-reigning British monarch before Queen Elizabeth II?",
                "a": "Queen Victoria",
                "b": "King George III",
                "c": "Queen Mary I",
                "d": "Queen Elizabeth I",
                "correct": "Queen Victoria",
                "speak": "Queen Victoria"
            },
            {
                "question": "Which empire did Genghis Khan establish?",
                "a": "Roman Empire",
                "b": "Mongol Empire",
                "c": "Ottoman Empire",
                "d": "Persian Empire",
                "correct": "Mongol Empire",
                "speak": "Mongol Empire"
            },
            {
                "question": "In which year did the Berlin Wall fall?",
                "a": "1987",
                "b": "1988",
                "c": "1989",
                "d": "1990",
                "correct": "1989",
                "speak": "1989"
            },
            {
                "question": "Who was the first female Prime Minister of the United Kingdom?",
                "a": "Margaret Thatcher",
                "b": "Theresa May",
                "c": "Indira Gandhi",
                "d": "Angela Merkel",
                "correct": "Margaret Thatcher",
                "speak": "Margaret Thatcher"
            },
            {
                "question": "What was the name of the ship on which the Pilgrims traveled to America?",
                "a": "Mayflower",
                "b": "Santa Maria",
                "c": "Pinta",
                "d": "Nina",
                "correct": "Mayflower",
                "speak": "Mayflower"
            },
            {
                "question": "Who was assassinated on November 22, 1963?",
                "a": "Martin Luther King Jr.",
                "b": "Robert F. Kennedy",
                "c": "John F. Kennedy",
                "d": "Malcolm X",
                "correct": "John F. Kennedy",
                "speak": "John F. Kennedy"
            },
            {
                "question": "Which war was fought between the North and South regions in the United States?",
                "a": "World War I",
                "b": "World War II",
                "c": "The Civil War",
                "d": "The Revolutionary War",
                "correct": "The Civil War",
                "speak": "The Civil War"
            },
            {
                "question": "Who was the leader of the Soviet Union during World War II?",
                "a": "Vladimir Lenin",
                "b": "Joseph Stalin",
                "c": "Nikita Khrushchev",
                "d": "Leonid Brezhnev",
                "correct": "Joseph Stalin",
                "speak": "Joseph Stalin"
            },
            {
                "question": "In which year did the Titanic sink?",
                "a": "1908",
                "b": "1910",
                "c": "1912",
                "d": "1914",
                "correct": "1912",
                "speak": "1912"
            },
            {
                "question": "Who wrote the Communist Manifesto?",
                "a": "Karl Marx",
                "b": "Vladimir Lenin",
                "c": "Friedrich Engels",
                "d": "Mao Zedong",
                "correct": "Karl Marx",
                "speak": "Karl Marx"
            },
            {
                "question": "Which country was Adolf Hitler born in?",
                "a": "Germany",
                "b": "Austria",
                "c": "Poland",
                "d": "Hungary",
                "correct": "Austria",
                "speak": "Austria"
            },
            {
                "question": "Which ancient civilization was known for its philosophers like Socrates and Plato?",
                "a": "Roman",
                "b": "Greek",
                "c": "Egyptian",
                "d": "Chinese",
                "correct": "Greek",
                "speak": "Greek"
            },
            {
                "question": "What year did the United States land the first man on the moon?",
                "a": "1967",
                "b": "1968",
                "c": "1969",
                "d": "1970",
                "correct": "1969",
                "speak": "1969"
            },
            {
                "question": "Who was the British Prime Minister during World War II?",
                "a": "Neville Chamberlain",
                "b": "Winston Churchill",
                "c": "Clement Attlee",
                "d": "Harold Macmillan",
                "correct": "Winston Churchill",
                "speak": "Winston Churchill"
            },
            {
                "question": "Which famous queen had six husbands?",
                "a": "Elizabeth I",
                "b": "Mary I",
                "c": "Catherine the Great",
                "d": "Henry VIII",
                "correct": "Henry VIII",
                "speak": "Henry VIII"
            },
            {
                "question": "In which year did the Soviet Union collapse?",
                "a": "1989",
                "b": "1990",
                "c": "1991",
                "d": "1992",
                "correct": "1991",
                "speak": "1991"
            },
            {
                "question": "Who was the first emperor of China?",
                "a": "Qin Shi Huang",
                "b": "Liu Bang",
                "c": "Genghis Khan",
                "d": "Kublai Khan",
                "correct": "Qin Shi Huang",
                "speak": "Qin Shi Huang"
            },
            {
                "question": "Which ancient civilization is credited with inventing the wheel?",
                "a": "Egyptians",
                "b": "Greeks",
                "c": "Sumerians",
                "d": "Romans",
                "correct": "Sumerians",
                "speak": "Sumerians"
            },
            {
                "question": "Who was the last Tsar of Russia?",
                "a": "Alexander III",
                "b": "Nicholas II",
                "c": "Peter the Great",
                "d": "Ivan the Terrible",
                "correct": "Nicholas II",
                "speak": "Nicholas II"
            },
            {
                "question": "What was the main purpose of the Great Wall of China?",
                "a": "Trade",
                "b": "Transportation",
                "c": "Defense",
                "d": "Agriculture",
                "correct": "Defense",
                "speak": "Defense"
            },
            {
                "question": "Which U.S. President issued the Emancipation Proclamation?",
                "a": "George Washington",
                "b": "Thomas Jefferson",
                "c": "Abraham Lincoln",
                "d": "Theodore Roosevelt",
                "correct": "Abraham Lincoln",
                "speak": "Abraham Lincoln"
            },
            {
                "question": "Who is the President of the United States as of 2023?",
                "a": "Donald Trump",
                "b": "Joe Biden",
                "c": "Barack Obama",
                "d": "George W. Bush",
                "correct": "Joe Biden",
                "speak": "Joe Biden"
            },
            {
                "question": "Which country recently left the European Union?",
                "a": "France",
                "b": "Germany",
                "c": "United Kingdom",
                "d": "Italy",
                "correct": "United Kingdom",
                "speak": "United Kingdom"
            },
            {
                "question": "Which country hosted the 2022 Winter Olympics?",
                "a": "Russia",
                "b": "Japan",
                "c": "China",
                "d": "South Korea",
                "correct": "China",
                "speak": "China"
            },
            {
                "question": "What is the capital city of Australia?",
                "a": "Sydney",
                "b": "Melbourne",
                "c": "Canberra",
                "d": "Brisbane",
                "correct": "Canberra",
                "speak": "Canberra"
            },
            {
                "question": "Which country has the world's largest economy?",
                "a": "China",
                "b": "United States",
                "c": "Japan",
                "d": "Germany",
                "correct": "United States",
                "speak": "United States"
            },
            {
                "question": "Which African country recently elected its first female president?",
                "a": "Liberia",
                "b": "Ethiopia",
                "c": "Ghana",
                "d": "Tanzania",
                "correct": "Tanzania",
                "speak": "Tanzania"
            },
            {
                "question": "What is the name of the political party founded by Emmanuel Macron?",
                "a": "The Republicans",
                "b": "Socialist Party",
                "c": "La République En Marche!",
                "d": "National Rally",
                "correct": "La République En Marche!",
                "speak": "La République En Marche!"
            },
            {
                "question": "Which country is known for its policy of neutrality?",
                "a": "Switzerland",
                "b": "Sweden",
                "c": "Norway",
                "d": "Finland",
                "correct": "Switzerland",
                "speak": "Switzerland"
            },
            {
                "question": "Which international organization is headquartered in New York City?",
                "a": "NATO",
                "b": "United Nations",
                "c": "European Union",
                "d": "World Bank",
                "correct": "United Nations",
                "speak": "United Nations"
            },
            {
                "question": "Which country recently held a referendum on independence in 2017?",
                "a": "Catalonia (Spain)",
                "b": "Scotland (UK)",
                "c": "Quebec (Canada)",
                "d": "Tibet (China)",
                "correct": "Catalonia (Spain)",
                "speak": "Catalonia (Spain)"
            },
            {
                "question": "Who is the current Prime Minister of the United Kingdom?",
                "a": "Boris Johnson",
                "b": "Theresa May",
                "c": "David Cameron",
                "d": "Rishi Sunak",
                "correct": "Rishi Sunak",
                "speak": "Rishi Sunak"
            },
            {
                "question": "Which country is the largest producer of crude oil?",
                "a": "Russia",
                "b": "Saudi Arabia",
                "c": "United States",
                "d": "Iran",
                "correct": "United States",
                "speak": "United States"
            },
            {
                "question": "Which country is known for its strict internet censorship policies?",
                "a": "North Korea",
                "b": "China",
                "c": "Iran",
                "d": "Saudi Arabia",
                "correct": "China",
                "speak": "China"
            },
            {
                "question": "Which country has the highest population in the world?",
                "a": "India",
                "b": "United States",
                "c": "China",
                "d": "Indonesia",
                "correct": "India",
                "speak": "India"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "a": "Yuan",
                "b": "Won",
                "c": "Yen",
                "d": "Ruble",
                "correct": "Yen",
                "speak": "Yen"
            },
            {
                "question": "Which country is the largest democracy in the world?",
                "a": "United States",
                "b": "India",
                "c": "Brazil",
                "d": "Indonesia",
                "correct": "India",
                "speak": "India"
            },
            {
                "question": "Who is the President of South Africa?",
                "a": "Nelson Mandela",
                "b": "Jacob Zuma",
                "c": "Cyril Ramaphosa",
                "d": "Thabo Mbeki",
                "correct": "Cyril Ramaphosa",
                "speak": "Cyril Ramaphosa"
            },
            {
                "question": "Which organization is responsible for regulating international trade?",
                "a": "IMF",
                "b": "World Bank",
                "c": "WTO",
                "d": "UNESCO",
                "correct": "WTO",
                "speak": "WTO"
            },
            {
                "question": "Which country is the largest producer of coffee?",
                "a": "Colombia",
                "b": "Vietnam",
                "c": "Brazil",
                "d": "Ethiopia",
                "correct": "Brazil",
                "speak": "Brazil"
            },
            {
                "question": "Which Middle Eastern country has been in a civil war since 2011?",
                "a": "Iraq",
                "b": "Syria",
                "c": "Libya",
                "d": "Yemen",
                "correct": "Syria",
                "speak": "Syria"
            },
            {
                "question": "Who wrote 'Moby-Dick'?",
                "a": "Herman Melville",
                "b": "Mark Twain",
                "c": "Nathaniel Hawthorne",
                "d": "Edgar Allan Poe",
                "correct": "Herman Melville",
                "speak": "Herman Melville"
            },
            {
                "question": "Who is the author of '1984'?",
                "a": "Aldous Huxley",
                "b": "George Orwell",
                "c": "Ray Bradbury",
                "d": "Isaac Asimov",
                "correct": "George Orwell",
                "speak": "George Orwell"
            },
            {
                "question": "Which novel begins with the line, 'Call me Ishmael'?",
                "a": "Moby-Dick",
                "b": "The Scarlet Letter",
                "c": "Great Expectations",
                "d": "War and Peace",
                "correct": "Moby-Dick",
                "speak": "Moby-Dick"
            },
            {
                "question": "Who wrote 'The Great Gatsby'?",
                "a": "F. Scott Fitzgerald",
                "b": "Ernest Hemingway",
                "c": "John Steinbeck",
                "d": "William Faulkner",
                "correct": "F. Scott Fitzgerald",
                "speak": "F. Scott Fitzgerald"
            },
            {
                "question": "Who is the author of 'Pride and Prejudice'?",
                "a": "Emily Brontë",
                "b": "Jane Austen",
                "c": "Mary Shelley",
                "d": "Charlotte Brontë",
                "correct": "Jane Austen",
                "speak": "Jane Austen"
            },
            {
                "question": "Which Shakespeare play features the characters Rosencrantz and Guildenstern?",
                "a": "Hamlet",
                "b": "Macbeth",
                "c": "Othello",
                "d": "King Lear",
                "correct": "Hamlet",
                "speak": "Hamlet"
            },
            {
                "question": "Who wrote 'The Catcher in the Rye'?",
                "a": "J.D. Salinger",
                "b": "Harper Lee",
                "c": "J.K. Rowling",
                "d": "John Steinbeck",
                "correct": "J.D. Salinger",
                "speak": "J.D. Salinger"
            },
            {
                "question": "Which novel features the character Atticus Finch?",
                "a": "To Kill a Mockingbird",
                "b": "The Great Gatsby",
                "c": "Catch-22",
                "d": "The Grapes of Wrath",
                "correct": "To Kill a Mockingbird",
                "speak": "To Kill a Mockingbird"
            },
            {
                "question": "Who is the author of 'The Hobbit'?",
                "a": "C.S. Lewis",
                "b": "J.R.R. Tolkien",
                "c": "George R.R. Martin",
                "d": "Terry Pratchett",
                "correct": "J.R.R. Tolkien",
                "speak": "J.R.R. Tolkien"
            },
            {
                "question": "Which poet wrote 'The Raven'?",
                "a": "Robert Frost",
                "b": "Walt Whitman",
                "c": "Edgar Allan Poe",
                "d": "Emily Dickinson",
                "correct": "Edgar Allan Poe",
                "speak": "Edgar Allan Poe"
            },
            {
                "question": "Who wrote 'Brave New World'?",
                "a": "George Orwell",
                "b": "Aldous Huxley",
                "c": "Ray Bradbury",
                "d": "Kurt Vonnegut",
                "correct": "Aldous Huxley",
                "speak": "Aldous Huxley"
            },
            {
                "question": "Who is the author of 'Harry Potter'?",
                "a": "J.K. Rowling",
                "b": "Suzanne Collins",
                "c": "Stephen King",
                "d": "Rick Riordan",
                "correct": "J.K. Rowling",
                "speak": "J.K. Rowling"
            },
            {
                "question": "Which novel features the character Elizabeth Bennet?",
                "a": "Sense and Sensibility",
                "b": "Pride and Prejudice",
                "c": "Emma",
                "d": "Persuasion",
                "correct": "Pride and Prejudice",
                "speak": "Pride and Prejudice"
            },
            {
                "question": "Who wrote 'The Odyssey'?",
                "a": "Homer",
                "b": "Virgil",
                "c": "Sophocles",
                "d": "Euripides",
                "correct": "Homer",
                "speak": "Homer"
            },
            {
                "question": "Which novel begins with the line, 'It was the best of times, it was the worst of times'?",
                "a": "Moby-Dick",
                "b": "A Tale of Two Cities",
                "c": "Great Expectations",
                "d": "The Scarlet Letter",
                "correct": "A Tale of Two Cities",
                "speak": "A Tale of Two Cities"
            },
            {
                "question": "Who wrote 'The Chronicles of Narnia'?",
                "a": "J.K. Rowling",
                "b": "J.R.R. Tolkien",
                "c": "C.S. Lewis",
                "d": "Philip Pullman",
                "correct": "C.S. Lewis",
                "speak": "C.S. Lewis"
            },
            {
                "question": "Which novel features the character Jay Gatsby?",
                "a": "The Great Gatsby",
                "b": "To Kill a Mockingbird",
                "c": "The Catcher in the Rye",
                "d": "The Grapes of Wrath",
                "correct": "The Great Gatsby",
                "speak": "The Great Gatsby"
            },
            {
                "question": "Who wrote 'Frankenstein'?",
                "a": "Mary Shelley",
                "b": "Bram Stoker",
                "c": "H.G. Wells",
                "d": "Jules Verne",
                "correct": "Mary Shelley",
                "speak": "Mary Shelley"
            },
            {
                "question": "Who is the author of 'The Lord of the Rings'?",
                "a": "George R.R. Martin",
                "b": "C.S. Lewis",
                "c": "J.K. Rowling",
                "d": "J.R.R. Tolkien",
                "correct": "J.R.R. Tolkien",
                "speak": "J.R.R. Tolkien"
            },
            {
                "question": "Which novel features the character Sherlock Holmes?",
                "a": "Dracula",
                "b": "The Hound of the Baskervilles",
                "c": "The Great Gatsby",
                "d": "To Kill a Mockingbird",
                "correct": "The Hound of the Baskervilles",
                "speak": "The Hound of the Baskervilles"
            },
            {
                "question": "Who wrote 'Dracula'?",
                "a": "Mary Shelley",
                "b": "Bram Stoker",
                "c": "H.G. Wells",
                "d": "Jules Verne",
                "correct": "Bram Stoker",
                "speak": "Bram Stoker"
            },
            {
                "question": "Who is the author of 'The Catch-22'?",
                "a": "Joseph Heller",
                "b": "Kurt Vonnegut",
                "c": "George Orwell",
                "d": "Aldous Huxley",
                "correct": "Joseph Heller",
                "speak": "Joseph Heller"
            },
            {
                "question": "Which novel features the character Huckleberry Finn?",
                "a": "The Adventures of Huckleberry Finn",
                "b": "The Catcher in the Rye",
                "c": "To Kill a Mockingbird",
                "d": "The Great Gatsby",
                "correct": "The Adventures of Huckleberry Finn",
                "speak": "The Adventures of Huckleberry Finn"
            },
            {
                "question": "Who wrote 'The Count of Monte Cristo'?",
                "a": "Jules Verne",
                "b": "Alexandre Dumas",
                "c": "Victor Hugo",
                "d": "Gustave Flaubert",
                "correct": "Alexandre Dumas",
                "speak": "Alexandre Dumas"
            },
            {
                "question": "Who is the author of 'War and Peace'?",
                "a": "Fyodor Dostoevsky",
                "b": "Leo Tolstoy",
                "c": "Anton Chekhov",
                "d": "Nikolai Gogol",
                "correct": "Leo Tolstoy",
                "speak": "Leo Tolstoy"
            },
            {
                "question": "Which novel features the character Frodo Baggins?",
                "a": "The Hobbit",
                "b": "The Silmarillion",
                "c": "The Lord of the Rings",
                "d": "The Chronicles of Narnia",
                "correct": "The Lord of the Rings",
                "speak": "The Lord of the Rings"
            },
            {
                "question": "Who wrote 'One Hundred Years of Solitude'?",
                "a": "Gabriel Garcia Marquez",
                "b": "Jorge Luis Borges",
                "c": "Mario Vargas Llosa",
                "d": "Isabel Allende",
                "correct": "Gabriel Garcia Marquez",
                "speak": "Gabriel Garcia Marquez"
            },
            {
                "question": "Who is the author of 'Don Quixote'?",
                "a": "Miguel de Cervantes",
                "b": "Jorge Luis Borges",
                "c": "Gabriel Garcia Marquez",
                "d": "Pablo Neruda",
                "correct": "Miguel de Cervantes",
                "speak": "Miguel de Cervantes"
            },
            {
                "question": "Which novel begins with the line, 'It was a bright cold day in April, and the clocks were striking thirteen'?",
                "a": "Brave New World",
                "b": "1984",
                "c": "Fahrenheit 451",
                "d": "The Handmaid's Tale",
                "correct": "1984",
                "speak": "1984"
            },
            {
                "question": "What is the chemical symbol for water?",
                "a": "H2",
                "b": "H2O",
                "c": "HO2",
                "d": "H2O2",
                "correct": "H2O",
                "speak": "H2O"
            },
            {
                "question": "What planet is known as the Red Planet?",
                "a": "Venus",
                "b": "Mars",
                "c": "Jupiter",
                "d": "Saturn",
                "correct": "Mars",
                "speak": "Mars"
            },
            {
                "question": "Who developed the theory of general relativity?",
                "a": "Isaac Newton",
                "b": "Albert Einstein",
                "c": "Niels Bohr",
                "d": "Galileo Galilei",
                "correct": "Albert Einstein",
                "speak": "Albert Einstein"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "a": "Nucleus",
                "b": "Ribosome",
                "c": "Mitochondria",
                "d": "Chloroplast",
                "correct": "Mitochondria",
                "speak": "Mitochondria"
            },
            {
                "question": "What is the speed of light?",
                "a": "300,000 km/s",
                "b": "150,000 km/s",
                "c": "200,000 km/s",
                "d": "250,000 km/s",
                "correct": "300,000 km/s",
                "speak": "300,000 km/s"
            },
            {
                "question": "Who is known as the father of modern physics?",
                "a": "Isaac Newton",
                "b": "Galileo Galilei",
                "c": "Albert Einstein",
                "d": "Niels Bohr",
                "correct": "Galileo Galilei",
                "speak": "Galileo Galilei"
            },
            {
                "question": "What is the most abundant gas in Earth's atmosphere?",
                "a": "Oxygen",
                "b": "Carbon Dioxide",
                "c": "Nitrogen",
                "d": "Hydrogen",
                "correct": "Nitrogen",
                "speak": "Nitrogen"
            },
            {
                "question": "Who discovered penicillin?",
                "a": "Alexander Fleming",
                "b": "Marie Curie",
                "c": "Louis Pasteur",
                "d": "Gregor Mendel",
                "correct": "Alexander Fleming",
                "speak": "Alexander Fleming"
            },
            {
                "question": "What is the smallest unit of life?",
                "a": "Atom",
                "b": "Molecule",
                "c": "Cell",
                "d": "Organism",
                "correct": "Cell",
                "speak": "Cell"
            },
            {
                "question": "What is the chemical formula for table salt?",
                "a": "NaCl",
                "b": "KCl",
                "c": "Na2SO4",
                "d": "K2SO4",
                "correct": "NaCl",
                "speak": "NaCl"
            },
            {
                "question": "Who proposed the laws of motion?",
                "a": "Albert Einstein",
                "b": "Galileo Galilei",
                "c": "Isaac Newton",
                "d": "Niels Bohr",
                "correct": "Isaac Newton",
                "speak": "Isaac Newton"
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "a": "Gold",
                "b": "Iron",
                "c": "Diamond",
                "d": "Quartz",
                "correct": "Diamond",
                "speak": "Diamond"
            },
            {
                "question": "What is the primary gas in the Sun's composition?",
                "a": "Oxygen",
                "b": "Hydrogen",
                "c": "Helium",
                "d": "Nitrogen",
                "correct": "Hydrogen",
                "speak": "Hydrogen"
            },
            {
                "question": "What element does 'O' represent on the periodic table?",
                "a": "Gold",
                "b": "Oxygen",
                "c": "Osmium",
                "d": "Oganesson",
                "correct": "Oxygen",
                "speak": "Oxygen"
            },
            {
                "question": "What is the pH of pure water?",
                "a": "5",
                "b": "6",
                "c": "7",
                "d": "8",
                "correct": "7",
                "speak": "7"
            },
            {
                "question": "What type of energy is stored in a battery?",
                "a": "Kinetic",
                "b": "Thermal",
                "c": "Chemical",
                "d": "Mechanical",
                "correct": "Chemical",
                "speak": "Chemical"
            },
            {
                "question": "Who is known for the laws of inheritance?",
                "a": "Charles Darwin",
                "b": "Gregor Mendel",
                "c": "Louis Pasteur",
                "d": "Alexander Fleming",
                "correct": "Gregor Mendel",
                "speak": "Gregor Mendel"
            },
            {
                "question": "What planet is closest to the Sun?",
                "a": "Venus",
                "b": "Mars",
                "c": "Mercury",
                "d": "Earth",
                "correct": "Mercury",
                "speak": "Mercury"
            },
            {
                "question": "What is the center of an atom called?",
                "a": "Electron",
                "b": "Proton",
                "c": "Nucleus",
                "d": "Neutron",
                "correct": "Nucleus",
                "speak": "Nucleus"
            },
            {
                "question": "What is the study of plants called?",
                "a": "Zoology",
                "b": "Geology",
                "c": "Botany",
                "d": "Ecology",
                "correct": "Botany",
                "speak": "Botany"
            },
            {
                "question": "What is the largest organ in the human body?",
                "a": "Heart",
                "b": "Liver",
                "c": "Skin",
                "d": "Lungs",
                "correct": "Skin",
                "speak": "Skin"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "a": "Ag",
                "b": "Au",
                "c": "Pb",
                "d": "Fe",
                "correct": "Au",
                "speak": "Au"
            },
            {
                "question": "What part of the cell contains the genetic material?",
                "a": "Cytoplasm",
                "b": "Mitochondria",
                "c": "Nucleus",
                "d": "Cell membrane",
                "correct": "Nucleus",
                "speak": "Nucleus"
            },
            {
                "question": "What force keeps us grounded on Earth?",
                "a": "Magnetism",
                "b": "Electromagnetism",
                "c": "Gravity",
                "d": "Friction",
                "correct": "Gravity",
                "speak": "Gravity"
            },
            {
                "question": "What is the most abundant element in the universe?",
                "a": "Oxygen",
                "b": "Hydrogen",
                "c": "Helium",
                "d": "Carbon",
                "correct": "Hydrogen",
                "speak": "Hydrogen"
            },
            {
                "question": "Who is known as the father of evolution?",
                "a": "Isaac Newton",
                "b": "Charles Darwin",
                "c": "Gregor Mendel",
                "d": "Albert Einstein",
                "correct": "Charles Darwin",
                "speak": "Charles Darwin"
            },
            {
                "question": "What is the chemical formula for carbon dioxide?",
                "a": "CO",
                "b": "CO2",
                "c": "C2O",
                "d": "O2",
                "correct": "CO2",
                "speak": "CO2"
            },
            {
                "question": "What is the study of stars and planets called?",
                "a": "Geology",
                "b": "Biology",
                "c": "Astronomy",
                "d": "Chemistry",
                "correct": "Astronomy",
                "speak": "Astronomy"
            },
            {
                "question": "Who developed the periodic table?",
                "a": "Marie Curie",
                "b": "Dmitri Mendeleev",
                "c": "Niels Bohr",
                "d": "Albert Einstein",
                "correct": "Dmitri Mendeleev",
                "speak": "Dmitri Mendeleev"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "a": "Earth",
                "b": "Saturn",
                "c": "Jupiter",
                "d": "Neptune",
                "correct": "Jupiter",
                "speak": "Jupiter"
            },
            {
                "question": "What is the most common gas in the Earth's atmosphere?",
                "a": "Oxygen",
                "b": "Carbon dioxide",
                "c": "Nitrogen",
                "d": "Hydrogen",
                "correct": "Nitrogen",
                "speak": "Nitrogen"
            },
            {
                "question": "What is the main gas found in the air we breathe?",
                "a": "Oxygen",
                "b": "Carbon Dioxide",
                "c": "Hydrogen",
                "d": "Nitrogen",
                "correct": "Nitrogen",
                "speak": "Nitrogen"
            },
            {
                "question": "Who is known as the father of genetics?",
                "a": "Charles Darwin",
                "b": "Gregor Mendel",
                "c": "Louis Pasteur",
                "d": "Alexander Fleming",
                "correct": "Gregor Mendel",
                "speak": "Gregor Mendel"
            },
            {
                "question": "What is the basic unit of life?",
                "a": "Atom",
                "b": "Molecule",
                "c": "Cell",
                "d": "Tissue",
                "correct": "Cell",
                "speak": "Cell"
            },
            {
                "question": "What is the capital of France?",
                "a": "Berlin",
                "b": "Madrid",
                "c": "Rome",
                "d": "Paris",
                "correct": "Paris",
                "speak": "Paris"
            },
            {
                "question": "Which is the largest continent by land area?",
                "a": "Africa",
                "b": "Asia",
                "c": "Europe",
                "d": "Antarctica",
                "correct": "Asia",
                "speak": "Asia"
            },
            {
                "question": "What is the longest river in the world?",
                "a": "Amazon River",
                "b": "Nile River",
                "c": "Yangtze River",
                "d": "Mississippi River",
                "correct": "Nile River",
                "speak": "Nile River"
            },
            {
                "question": "Mount Everest is located in which mountain range?",
                "a": "Andes",
                "b": "Rockies",
                "c": "Himalayas",
                "d": "Alps",
                "correct": "Himalayas",
                "speak": "Himalayas"
            },
            {
                "question": "What is the smallest country in the world by land area?",
                "a": "Monaco",
                "b": "San Marino",
                "c": "Liechtenstein",
                "d": "Vatican City",
                "correct": "Vatican City",
                "speak": "Vatican City"
            },
            {
                "question": "What is the capital of Australia?",
                "a": "Sydney",
                "b": "Melbourne",
                "c": "Brisbane",
                "d": "Canberra",
                "correct": "Canberra",
                "speak": "Canberra"
            },
            {
                "question": "Which country is the largest by land area?",
                "a": "Canada",
                "b": "United States",
                "c": "Russia",
                "d": "China",
                "correct": "Russia",
                "speak": "Russia"
            },
            {
                "question": "Which ocean is the deepest?",
                "a": "Atlantic Ocean",
                "b": "Indian Ocean",
                "c": "Arctic Ocean",
                "d": "Pacific Ocean",
                "correct": "Pacific Ocean",
                "speak": "Pacific Ocean"
            },
            {
                "question": "What is the longest mountain range in the world?",
                "a": "Rockies",
                "b": "Andes",
                "c": "Himalayas",
                "d": "Alps",
                "correct": "Andes",
                "speak": "Andes"
            },
            {
                "question": "Which country has the largest population?",
                "a": "India",
                "b": "United States",
                "c": "China",
                "d": "Indonesia",
                "correct": "China",
                "speak": "China"
            },
            {
                "question": "What is the capital of Canada?",
                "a": "Toronto",
                "b": "Vancouver",
                "c": "Ottawa",
                "d": "Montreal",
                "correct": "Ottawa",
                "speak": "Ottawa"
            },
            {
                "question": "Which is the largest island in the world?",
                "a": "Borneo",
                "b": "New Guinea",
                "c": "Greenland",
                "d": "Madagascar",
                "correct": "Greenland",
                "speak": "Greenland"
            },
            {
                "question": "What is the capital of Japan?",
                "a": "Seoul",
                "b": "Beijing",
                "c": "Tokyo",
                "d": "Kyoto",
                "correct": "Tokyo",
                "speak": "Tokyo"
            },
            {
                "question": "Which U.S. state is the largest by land area?",
                "a": "California",
                "b": "Texas",
                "c": "Alaska",
                "d": "Montana",
                "correct": "Alaska",
                "speak": "Alaska"
            },
            {
                "question": "Which is the smallest ocean in the world?",
                "a": "Atlantic Ocean",
                "b": "Indian Ocean",
                "c": "Southern Ocean",
                "d": "Arctic Ocean",
                "correct": "Arctic Ocean",
                "speak": "Arctic Ocean"
            },
            {
                "question": "What is the capital of Brazil?",
                "a": "Rio de Janeiro",
                "b": "São Paulo",
                "c": "Brasília",
                "d": "Salvador",
                "correct": "Brasília",
                "speak": "Brasília"
            },
            {
                "question": "Which river flows through Paris?",
                "a": "Thames",
                "b": "Seine",
                "c": "Danube",
                "d": "Rhine",
                "correct": "Seine",
                "speak": "Seine"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "a": "China",
                "b": "Japan",
                "c": "South Korea",
                "d": "Thailand",
                "correct": "Japan",
                "speak": "Japan"
            },
            {
                "question": "Which U.S. state is known as the Sunshine State?",
                "a": "California",
                "b": "Hawaii",
                "c": "Florida",
                "d": "Arizona",
                "correct": "Florida",
                "speak": "Florida"
            },
            {
                "question": "What is the capital of Italy?",
                "a": "Venice",
                "b": "Milan",
                "c": "Florence",
                "d": "Rome",
                "correct": "Rome",
                "speak": "Rome"
            },
            {
                "question": "Which continent has the most countries?",
                "a": "Asia",
                "b": "Africa",
                "c": "Europe",
                "d": "South America",
                "correct": "Africa",
                "speak": "Africa"
            },
            {
                "question": "What is the longest river in the United States?",
                "a": "Mississippi River",
                "b": "Missouri River",
                "c": "Colorado River",
                "d": "Yukon River",
                "correct": "Missouri River",
                "speak": "Missouri River"
            },
            {
                "question": "What is the capital of India?",
                "a": "Mumbai",
                "b": "Kolkata",
                "c": "New Delhi",
                "d": "Bangalore",
                "correct": "New Delhi",
                "speak": "New Delhi"
            },
            {
                "question": "Which European country is divided into departments?",
                "a": "Germany",
                "b": "Italy",
                "c": "France",
                "d": "Spain",
                "correct": "France",
                "speak": "France"
            },
            {
                "question": "What is the capital of Egypt?",
                "a": "Alexandria",
                "b": "Cairo",
                "c": "Giza",
                "d": "Luxor",
                "correct": "Cairo",
                "speak": "Cairo"
            },
            {
                "question": "Which country is known as the Land Down Under?",
                "a": "South Africa",
                "b": "New Zealand",
                "c": "Australia",
                "d": "Fiji",
                "correct": "Australia",
                "speak": "Australia"
            },
            {
                "question": "What is the capital of Russia?",
                "a": "St. Petersburg",
                "b": "Minsk",
                "c": "Moscow",
                "d": "Kiev",
                "correct": "Moscow",
                "speak": "Moscow"
            },
            {
                "question": "What is the highest mountain in Africa?",
                "a": "Mount Kenya",
                "b": "Mount Kilimanjaro",
                "c": "Mount Elgon",
                "d": "Mount Meru",
                "correct": "Mount Kilimanjaro",
                "speak": "Mount Kilimanjaro"
            },
            {
                "question": "Which country has the most time zones?",
                "a": "United States",
                "b": "Russia",
                "c": "China",
                "d": "Canada",
                "correct": "Russia",
                "speak": "Russia"
            },
            {
                "question": "Which country is the smallest by population?",
                "a": "Monaco",
                "b": "Nauru",
                "c": "San Marino",
                "d": "Vatican City",
                "correct": "Vatican City",
                "speak": "Vatican City"
            },
            {
                "question": "What is the capital of South Korea?",
                "a": "Tokyo",
                "b": "Seoul",
                "c": "Beijing",
                "d": "Pyongyang",
                "correct": "Seoul",
                "speak": "Seoul"
            },
            {
                "question": "What is the largest country in South America?",
                "a": "Argentina",
                "b": "Brazil",
                "c": "Peru",
                "d": "Colombia",
                "correct": "Brazil",
                "speak": "Brazil"
            },
            {
                "question": "Which sea is the saltiest?",
                "a": "Black Sea",
                "b": "Baltic Sea",
                "c": "Red Sea",
                "d": "Dead Sea",
                "correct": "Dead Sea",
                "speak": "Dead Sea"
            },
            {
                "question": "What is the capital of Sri Lanka?",
                "a": "Kandy",
                "b": "Galle",
                "c": "Colombo",
                "d": "Jaffna",
                "correct": "Colombo",
                "speak": "Colombo"
            },
            {
                "question": "What is the official language of Sri Lanka?",
                "a": "Hindi",
                "b": "English",
                "c": "Sinhala",
                "d": "Tamil",
                "correct": "Sinhala",
                "speak": "Sinhala"
            },
            {
                "question": "What is the traditional dress of Sri Lankan women called?",
                "a": "Sari",
                "b": "Kimono",
                "c": "Cheongsam",
                "d": "Hanbok",
                "correct": "Sari",
                "speak": "Sari"
            },
            {
                "question": "Which festival is known as the festival of lights in Sri Lanka?",
                "a": "Vesak",
                "b": "Diwali",
                "c": "Christmas",
                "d": "Ramadan",
                "correct": "Vesak",
                "speak": "Vesak"
            },
            {
                "question": "What is the national sport of Sri Lanka?",
                "a": "Cricket",
                "b": "Rugby",
                "c": "Volleyball",
                "d": "Football",
                "correct": "Volleyball",
                "speak": "Volleyball"
            },
            {
                "question": "Which famous tea comes from Sri Lanka?",
                "a": "Darjeeling",
                "b": "Assam",
                "c": "Ceylon",
                "d": "Earl Grey",
                "correct": "Ceylon",
                "speak": "Ceylon"
            },
            {
                "question": "What is the ancient capital city of Sri Lanka?",
                "a": "Kandy",
                "b": "Anuradhapura",
                "c": "Colombo",
                "d": "Galle",
                "correct": "Anuradhapura",
                "speak": "Anuradhapura"
            },
            {
                "question": "Which animal is featured in the Sri Lankan flag?",
                "a": "Elephant",
                "b": "Lion",
                "c": "Tiger",
                "d": "Peacock",
                "correct": "Lion",
                "speak": "Lion"
            },
            {
                "question": "What is a traditional Sri Lankan meal typically served on a banana leaf?",
                "a": "Thali",
                "b": "Dosa",
                "c": "Lamprais",
                "d": "Sushi",
                "correct": "Lamprais",
                "speak": "Lamprais"
            },
            {
                "question": "Which religion has the largest following in Sri Lanka?",
                "a": "Hinduism",
                "b": "Islam",
                "c": "Buddhism",
                "d": "Christianity",
                "correct": "Buddhism",
                "speak": "Buddhism"
            },
            {
                "question": "What is the name of the traditional Sri Lankan drum?",
                "a": "Tabla",
                "b": "Dhol",
                "c": "Thammattama",
                "d": "Djembe",
                "correct": "Thammattama",
                "speak": "Thammattama"
            },
            {
                "question": "What is the name of the famous Sri Lankan fortress built on a rock?",
                "a": "Sigiriya",
                "b": "Galle Fort",
                "c": "Polonnaruwa",
                "d": "Dambulla",
                "correct": "Sigiriya",
                "speak": "Sigiriya"
            },
            {
                "question": "What is the traditional dance form of the Kandyan region?",
                "a": "Bharatanatyam",
                "b": "Kathak",
                "c": "Kandyan dance",
                "d": "Odissi",
                "correct": "Kandyan dance",
                "speak": "Kandyan dance"
            },
            {
                "question": "Which Sri Lankan city is known for its sacred Temple of the Tooth?",
                "a": "Colombo",
                "b": "Galle",
                "c": "Kandy",
                "d": "Jaffna",
                "correct": "Kandy",
                "speak": "Kandy"
            },
            {
                "question": "What is the currency of Sri Lanka?",
                "a": "Rupee",
                "b": "Dollar",
                "c": "Pound",
                "d": "Euro",
                "correct": "Rupee",
                "speak": "Rupee"
            },
            {
                "question": "Which Sri Lankan festival celebrates the Sinhala and Tamil New Year?",
                "a": "Vesak",
                "b": "Poya",
                "c": "Avurudu",
                "d": "Deepavali",
                "correct": "Avurudu",
                "speak": "Avurudu"
            },
            {
                "question": "What is the name of the Sri Lankan martial art that includes both combat and dance?",
                "a": "Karate",
                "b": "Kalaripayattu",
                "c": "Angampora",
                "d": "Taekwondo",
                "correct": "Angampora",
                "speak": "Angampora"
            },
            {
                "question": "What is the main ingredient in the Sri Lankan dish 'Pol Sambol'?",
                "a": "Tomato",
                "b": "Coconut",
                "c": "Onion",
                "d": "Garlic",
                "correct": "Coconut",
                "speak": "Coconut"
            },
            {
                "question": "Which city is known as the 'Cultural Capital' of Sri Lanka?",
                "a": "Colombo",
                "b": "Kandy",
                "c": "Galle",
                "d": "Anuradhapura",
                "correct": "Kandy",
                "speak": "Kandy"
            },
            {
                "question": "What is the traditional Sri Lankan dance-drama called?",
                "a": "Kathakali",
                "b": "Bharatanatyam",
                "c": "Kohomba Kankariya",
                "d": "Yaksha Gana",
                "correct": "Kohomba Kankariya",
                "speak": "Kohomba Kankariya"
            },
            {
                "question": "What is the famous Sri Lankan mask dance form called?",
                "a": "Kandyan Dance",
                "b": "Kolam",
                "c": "Bharatanatyam",
                "d": "Odissi",
                "correct": "Kolam",
                "speak": "Kolam"
            },
            {
                "question": "Which Sri Lankan festival is celebrated with elephant parades and fire dances?",
                "a": "Diwali",
                "b": "Vesak",
                "c": "Esala Perahera",
                "d": "Avurudu",
                "correct": "Esala Perahera",
                "speak": "Esala Perahera"
            },
            {
                "question": "Which body of water lies to the west of Sri Lanka?",
                "a": "Bay of Bengal",
                "b": "Arabian Sea",
                "c": "Indian Ocean",
                "d": "Laccadive Sea",
                "correct": "Indian Ocean",
                "speak": "Indian Ocean"
            },
            {
                "question": "What is the national flower of Sri Lanka?",
                "a": "Lotus",
                "b": "Water Lily",
                "c": "Jasmine",
                "d": "Rose",
                "correct": "Water Lily",
                "speak": "Water Lily"
            },
            {
                "question": "Which Sri Lankan city is known for its Dutch colonial architecture?",
                "a": "Colombo",
                "b": "Kandy",
                "c": "Galle",
                "d": "Jaffna",
                "correct": "Galle",
                "speak": "Galle"
            },
            {
                "question": "What is the name of the traditional Sri Lankan rice and curry dish?",
                "a": "Biryani",
                "b": "Pulao",
                "c": "Lamprais",
                "d": "Kottu",
                "correct": "Lamprais",
                "speak": "Lamprais"
            },
            {
                "question": "Which festival marks the end of the Buddhist Lent in Sri Lanka?",
                "a": "Avurudu",
                "b": "Poya",
                "c": "Vesak",
                "d": "Poson",
                "correct": "Poson",
                "speak": "Poson"
            },
            {
                "question": "Which Sri Lankan dance is performed during the Kandyan festival?",
                "a": "Bharatanatyam",
                "b": "Kathak",
                "c": "Ves Dance",
                "d": "Yaksha Gana",
                "correct": "Ves Dance",
                "speak": "Ves Dance"
            },
            {
                "question": "What is the name of the traditional Sri Lankan drum used in folk music?",
                "a": "Tabla",
                "b": "Thammattama",
                "c": "Djembe",
                "d": "Mridangam",
                "correct": "Thammattama",
                "speak": "Thammattama"
            },
            {
                "question": "Which Sri Lankan festival is celebrated with lanterns and pandals?",
                "a": "Diwali",
                "b": "Vesak",
                "c": "Avurudu",
                "d": "Christmas",
                "correct": "Vesak",
                "speak": "Vesak"
            },
            {
                "question": "What is the name of the Sri Lankan traditional healing system?",
                "a": "Ayurveda",
                "b": "Homeopathy",
                "c": "Naturopathy",
                "d": "Acupuncture",
                "correct": "Ayurveda",
                "speak": "Ayurveda"
            },
            {
                "question": "Who wrote the novel 'Madol Doova'?",
                "a": "Martin Wickramasinghe",
                "b": "Gunadasa Amarasekara",
                "c": "Ediriweera Sarachchandra",
                "d": "T. B. Ilangaratne",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Who is the author of 'Viragaya'?",
                "a": "W. A. Silva",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Ediriweera Sarachchandra",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Which book is considered one of the greatest works of Sinhala literature, written by Kumaratunga Munidasa?",
                "a": "Koggala",
                "b": "Kumudini",
                "c": "Wesantara",
                "d": "Pujavaliya",
                "correct": "Koggala",
                "speak": "Koggala"
            },
            {
                "question": "Who wrote the Sinhala novel 'Yuganthaya'?",
                "a": "Martin Wickramasinghe",
                "b": "Gunadasa Amarasekara",
                "c": "Ediriweera Sarachchandra",
                "d": "Kumaratunga Munidasa",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Who is the famous Sri Lankan author known for the work 'Gamperaliya'?",
                "a": "Martin Wickramasinghe",
                "b": "Ediriweera Sarachchandra",
                "c": "Gunadasa Amarasekara",
                "d": "W. A. Silva",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan playwright wrote 'Maname'?",
                "a": "Sarachchandra",
                "b": "Kumaratunga Munidasa",
                "c": "Martin Wickramasinghe",
                "d": "W. A. Silva",
                "correct": "Sarachchandra",
                "speak": "Sarachchandra"
            },
            {
                "question": "Who is the author of 'Sanda Kinduru'?",
                "a": "Martin Wickramasinghe",
                "b": "Gunadasa Amarasekara",
                "c": "Kumaratunga Munidasa",
                "d": "Ediriweera Sarachchandra",
                "correct": "Ediriweera Sarachchandra",
                "speak": "Ediriweera Sarachchandra"
            },
            {
                "question": "Who wrote the novel 'Kalae Handa'?",
                "a": "W. A. Silva",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Ediriweera Sarachchandra",
                "correct": "W. A. Silva",
                "speak": "W. A. Silva"
            },
            {
                "question": "Who wrote the Sinhala novel 'Raththaran'?",
                "a": "Martin Wickramasinghe",
                "b": "W. A. Silva",
                "c": "Ediriweera Sarachchandra",
                "d": "Kumaratunga Munidasa",
                "correct": "W. A. Silva",
                "speak": "W. A. Silva"
            },
            {
                "question": "Which author is known for the work 'The Way of the Lotus'?",
                "a": "Kumaratunga Munidasa",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Ediriweera Sarachchandra",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Who is the famous Sri Lankan poet known for the collection 'Dolosmahe Pahana'?",
                "a": "Ediriweera Sarachchandra",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Mahagama Sekara",
                "correct": "Mahagama Sekara",
                "speak": "Mahagama Sekara"
            },
            {
                "question": "Which Sri Lankan writer is known for the novel 'Bambaru Avith'?",
                "a": "Gunadasa Amarasekara",
                "b": "Martin Wickramasinghe",
                "c": "Ediriweera Sarachchandra",
                "d": "Kumaratunga Munidasa",
                "correct": "Gunadasa Amarasekara",
                "speak": "Gunadasa Amarasekara"
            },
            {
                "question": "Who is the author of the work 'He Comes from Jaffna'?",
                "a": "Sarachchandra",
                "b": "Martin Wickramasinghe",
                "c": "Kumaratunga Munidasa",
                "d": "Sivagurunathan",
                "correct": "Sarachchandra",
                "speak": "Sarachchandra"
            },
            {
                "question": "Who wrote the collection of short stories 'The Water Diviner'?",
                "a": "Martin Wickramasinghe",
                "b": "Ediriweera Sarachchandra",
                "c": "Gunadasa Amarasekara",
                "d": "Kumaratunga Munidasa",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Who is the author of 'Araliya Mal Aramaya'?",
                "a": "Ediriweera Sarachchandra",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Kumaratunga Munidasa",
                "correct": "Ediriweera Sarachchandra",
                "speak": "Ediriweera Sarachchandra"
            },
            {
                "question": "Who wrote the novel 'Dahasak Sithuvili'?",
                "a": "Gunadasa Amarasekara",
                "b": "Ediriweera Sarachchandra",
                "c": "Martin Wickramasinghe",
                "d": "W. A. Silva",
                "correct": "Gunadasa Amarasekara",
                "speak": "Gunadasa Amarasekara"
            },
            {
                "question": "Who is the famous Sri Lankan poet known for the work 'Hathpana'?",
                "a": "Martin Wickramasinghe",
                "b": "W. A. Silva",
                "c": "Gunadasa Amarasekara",
                "d": "Kumaratunga Munidasa",
                "correct": "Kumaratunga Munidasa",
                "speak": "Kumaratunga Munidasa"
            },
            {
                "question": "Which Sri Lankan author wrote 'Viragaya'?",
                "a": "Ediriweera Sarachchandra",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Kumaratunga Munidasa",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Who wrote the Sinhala novel 'Koggala'?",
                "a": "Kumaratunga Munidasa",
                "b": "Ediriweera Sarachchandra",
                "c": "Martin Wickramasinghe",
                "d": "Gunadasa Amarasekara",
                "correct": "Kumaratunga Munidasa",
                "speak": "Kumaratunga Munidasa"
            },
            {
                "question": "Who is the author of the famous work 'Golu Hadawatha'?",
                "a": "Martin Wickramasinghe",
                "b": "W. A. Silva",
                "c": "Kumaratunga Munidasa",
                "d": "Karunasena Jayalath",
                "correct": "Karunasena Jayalath",
                "speak": "Karunasena Jayalath"
            },
            {
                "question": "Which Sri Lankan writer is known for the novel 'Gehenu Lamai'?",
                "a": "Martin Wickramasinghe",
                "b": "Gunadasa Amarasekara",
                "c": "Kumaratunga Munidasa",
                "d": "Karunasena Jayalath",
                "correct": "Karunasena Jayalath",
                "speak": "Karunasena Jayalath"
            },
            {
                "question": "Who is the author of 'Ape Gama'?",
                "a": "Ediriweera Sarachchandra",
                "b": "Martin Wickramasinghe",
                "c": "Gunadasa Amarasekara",
                "d": "Kumaratunga Munidasa",
                "correct": "Martin Wickramasinghe",
                "speak": "Martin Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan company is known for its innovations in mobile communication?",
                "a": "Mobitel",
                "b": "Dialog Axiata",
                "c": "Sri Lanka Telecom",
                "d": "Hutch",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "What is the name of the first satellite launched by Sri Lanka?",
                "a": "Ravana-1",
                "b": "Sakthi-1",
                "c": "LankaSat",
                "d": "Sathya-1",
                "correct": "Ravana-1",
                "speak": "Ravana-1"
            },
            {
                "question": "Which Sri Lankan university is known for its strong engineering and technology programs?",
                "a": "University of Colombo",
                "b": "University of Peradeniya",
                "c": "University of Moratuwa",
                "d": "University of Jaffna",
                "correct": "University of Moratuwa",
                "speak": "University of Moratuwa"
            },
            {
                "question": "Who is the founder of the Sri Lankan software company WSO2?",
                "a": "Sanjiva Weerawarana",
                "b": "Harsha Purasinghe",
                "c": "Madu Ratnayake",
                "d": "Suren Amarasekera",
                "correct": "Sanjiva Weerawarana",
                "speak": "Sanjiva Weerawarana"
            },
            {
                "question": "What is the main focus of the Sri Lankan tech company hSenid?",
                "a": "Telecommunications",
                "b": "E-commerce",
                "c": "Human Resource Solutions",
                "d": "Artificial Intelligence",
                "correct": "Human Resource Solutions",
                "speak": "Human Resource Solutions"
            },
            {
                "question": "Which Sri Lankan city is known as the 'ilicon Valley of Sri Lanka'?",
                "a": "Colombo",
                "b": "Kandy",
                "c": "Jaffna",
                "d": "Moratuwa",
                "correct": "Moratuwa",
                "speak": "Moratuwa"
            },
            {
                "question": "Which Sri Lankan company developed the app 'pickMe'?",
                "a": "Dialog Axiata",
                "b": "hSenid",
                "c": "PickMe Lanka",
                "d": "Kapruka",
                "correct": "PickMe Lanka",
                "speak": "PickMe Lanka"
            },
            {
                "question": "Which tech park is located in Malabe, Sri Lanka?",
                "a": "Trace City",
                "b": "Orion City",
                "c": "Tech City",
                "d": "Park City",
                "correct": "Trace City",
                "speak": "Trace City"
            },
            {
                "question": "What is the name of the first IT degree-awarding institute in Sri Lanka?",
                "a": "SLIIT",
                "b": "NSBM Green University",
                "c": "University of Colombo School of Computing",
                "d": "ESOFT Metro Campus",
                "correct": "SLIIT",
                "speak": "SLIIT"
            },
            {
                "question": "Which Sri Lankan tech company is known for its e-commerce platform?",
                "a": "Kapruka",
                "b": "WSO2",
                "c": "hSenid",
                "d": "MillenniumIT",
                "correct": "Kapruka",
                "speak": "Kapruka"
            },
            {
                "question": "Who is the founder of the e-commerce company Kapruka?",
                "a": "Sanjiva Weerawarana",
                "b": "Dulith Herath",
                "c": "Harsha Purasinghe",
                "d": "Ashanthi Koralage",
                "correct": "Dulith Herath",
                "speak": "Dulith Herath"
            },
            {
                "question": "Which Sri Lankan company specializes in stock exchange technology solutions?",
                "a": "WSO2",
                "b": "MillenniumIT",
                "c": "Dialog Axiata",
                "d": "Mobitel",
                "correct": "MillenniumIT",
                "speak": "MillenniumIT"
            },
            {
                "question": "Which organization is responsible for the development of information and communication technology in Sri Lanka?",
                "a": "ICTA",
                "b": "SLASSCOM",
                "c": "Sri Lanka Telecom",
                "d": "TRCSL",
                "correct": "ICTA",
                "speak": "ICTA"
            },
            {
                "question": "Which Sri Lankan company is known for its cloud-based Human Resource solutions?",
                "a": "WSO2",
                "b": "hSenid",
                "c": "MillenniumIT",
                "d": "Kapruka",
                "correct": "hSenid",
                "speak": "hSenid"
            },
            {
                "question": "What is the main purpose of the 'Digital Sri Lanka' initiative?",
                "a": "To enhance e-commerce",
                "b": "To improve internet connectivity",
                "c": "To digitize government services",
                "d": "To promote tech startups",
                "correct": "To digitize government services",
                "speak": "To digitize government services"
            },
            {
                "question": "Which Sri Lankan university offers a specialized degree in Mechatronics Engineering?",
                "a": "University of Peradeniya",
                "b": "University of Moratuwa",
                "c": "University of Colombo",
                "d": "University of Jaffna",
                "correct": "University of Moratuwa",
                "speak": "University of Moratuwa"
            },
            {
                "question": "Which Sri Lankan tech startup is known for its online payment gateway solutions?",
                "a": "hSenid",
                "b": "PayHere",
                "c": "WSO2",
                "d": "PickMe",
                "correct": "PayHere",
                "speak": "PayHere"
            },
            {
                "question": "Which mobile operator in Sri Lanka launched the first 4G LTE network?",
                "a": "Mobitel",
                "b": "Dialog Axiata",
                "c": "Hutch",
                "d": "Sri Lanka Telecom",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "Which tech event is considered the largest IT conference in Sri Lanka?",
                "a": "SLASSCOM Tech Conference",
                "b": "Disrupt Asia",
                "c": "Infotel",
                "d": "Echelon",
                "correct": "Disrupt Asia",
                "speak": "Disrupt Asia"
            },
            {
                "question": "What is the focus of the 'Trace Expert City' in Colombo?",
                "a": "E-commerce",
                "b": "Software Development",
                "c": "Startups and Innovation",
                "d": "Telecommunications",
                "correct": "Startups and Innovation",
                "speak": "Startups and Innovation"
            },
            {
                "question": "Which Sri Lankan tech company provides capital market software for stock exchanges worldwide?",
                "a": "MillenniumIT",
                "b": "WSO2",
                "c": "hSenid",
                "d": "PayHere",
                "correct": "MillenniumIT",
                "speak": "MillenniumIT"
            },
            {
                "question": "Which Sri Lankan city hosts the headquarters of Dialog Axiata?",
                "a": "Kandy",
                "b": "Colombo",
                "c": "Galle",
                "d": "Jaffna",
                "correct": "Colombo",
                "speak": "Colombo"
            },
            {
                "question": "Which tech park in Colombo is known for housing tech startups and innovation centers?",
                "a": "Orion City",
                "b": "Tech City",
                "c": "Park City",
                "d": "Trace City",
                "correct": "Orion City",
                "speak": "Orion City"
            },
            {
                "question": "Which Sri Lankan company is known for developing the electronic ticketing system for public transport?",
                "a": "MillenniumIT",
                "b": "Dialog Axiata",
                "c": "hSenid",
                "d": "SLT",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "Who is the founder of MillenniumIT, the Sri Lankan tech company?",
                "a": "Tony Weerasinghe",
                "b": "Sanjiva Weerawarana",
                "c": "Harsha Purasinghe",
                "d": "Dulith Herath",
                "correct": "Tony Weerasinghe",
                "speak": "Tony Weerasinghe"
            },
            {
                "question": "Which Sri Lankan company specializes in open-source middleware solutions?",
                "a": "hSenid",
                "b": "MillenniumIT",
                "c": "WSO2",
                "d": "Dialog Axiata",
                "correct": "WSO2",
                "speak": "WSO2"
            },
            {
                "question": "Which Sri Lankan tech company is a pioneer in online grocery delivery services?",
                "a": "Kapruka",
                "b": "PickMe",
                "c": "WSO2",
                "d": "hSenid",
                "correct": "Kapruka",
                "speak": "Kapruka"
            },
            {
                "question": "Which Sri Lankan university has a dedicated Faculty of Information Technology?",
                "a": "University of Colombo",
                "b": "University of Peradeniya",
                "c": "University of Moratuwa",
                "d": "University of Ruhuna",
                "correct": "University of Moratuwa",
                "speak": "University of Moratuwa"
            },
            {
                "question": "Who is considered one of the greatest cricketers in Sri Lankan history and is the leading wicket-taker in Test cricket?",
                "a": "Arjuna Ranatunga",
                "b": "Sanath Jayasuriya",
                "c": "Kumar Sangakkara",
                "d": "Muttiah Muralitharan",
                "correct": "Muttiah Muralitharan",
                "speak": "Muttiah Muralitharan"
            },
            {
                "question": "Which Sri Lankan cricketer scored 374 runs in a Test match, the highest individual score by a Sri Lankan?",
                "a": "Kumar Sangakkara",
                "b": "Mahela Jayawardene",
                "c": "Sanath Jayasuriya",
                "d": "Aravinda de Silva",
                "correct": "Mahela Jayawardene",
                "speak": "Mahela Jayawardene"
            },
            {
                "question": "Who captained the Sri Lankan cricket team to its first and only ICC Cricket World Cup victory in 1996?",
                "a": "Arjuna Ranatunga",
                "b": "Sanath Jayasuriya",
                "c": "Kumar Sangakkara",
                "d": "Marvan Atapattu",
                "correct": "Arjuna Ranatunga",
                "speak": "Arjuna Ranatunga"
            },
            {
                "question": "Which Sri Lankan sprinter won a silver medal in the 200m at the 2000 Sydney Olympics?",
                "a": "Susanthika Jayasinghe",
                "b": "Duncan White",
                "c": "Nimmi de Silva",
                "d": "Sugath Thilakaratne",
                "correct": "Susanthika Jayasinghe",
                "speak": "Susanthika Jayasinghe"
            },
            {
                "question": "Which sport is widely considered the national sport of Sri Lanka?",
                "a": "Cricket",
                "b": "Volleyball",
                "c": "Rugby",
                "d": "Football",
                "correct": "Volleyball",
                "speak": "Volleyball"
            },
            {
                "question": "Who was the first Sri Lankan to win a medal at the Olympics?",
                "a": "Susanthika Jayasinghe",
                "b": "Duncan White",
                "c": "Nimmi de Silva",
                "d": "Sugath Thilakaratne",
                "correct": "Duncan White",
                "speak": "Duncan White"
            },
            {
                "question": "Which Sri Lankan cricketer is holds the record for the fastest fifty in ODI cricket?",
                "a": "Sanath Jayasuriya",
                "b": "Kumar Sangakkara",
                "c": "Tillakaratne Dilshan",
                "d": "Thisara Perera",
                "correct": "Sanath Jayasuriya",
                "speak": "Sanath Jayasuriya"
            },
            {
                "question": "Who is the first Sri Lankan cricketer to score 10,000 runs in Test cricket?",
                "a": "Mahela Jayawardene",
                "b": "Kumar Sangakkara",
                "c": "Sanath Jayasuriya",
                "d": "Aravinda de Silva",
                "correct": "Kumar Sangakkara",
                "speak": "Kumar Sangakkara"
            },
            {
                "question": "Which Sri Lankan athlete is known for her achievements in the high jump and has won multiple medals at the South Asian Games?",
                "a": "Nimmi de Silva",
                "b": "Duncan White",
                "c": "Susanthika Jayasinghe",
                "d": "Sugath Thilakaratne",
                "correct": "Nimmi de Silva",
                "speak": "Nimmi de Silva"
            },
            {
                "question": "Which Sri Lankan cricketer is famous for inventing the 'Dilscoop' shot?",
                "a": "Mahela Jayawardene",
                "b": "Sanath Jayasuriya",
                "c": "Tillakaratne Dilshan",
                "d": "Aravinda de Silva",
                "correct": "Tillakaratne Dilshan",
                "speak": "Tillakaratne Dilshan"
            },
            {
                "question": "Who was the first Sri Lankan to play in the Indian Premier League (IPL)?",
                "a": "Sanath Jayasuriya",
                "b": "Muttiah Muralitharan",
                "c": "Kumar Sangakkara",
                "d": "Mahela Jayawardene",
                "correct": "Sanath Jayasuriya",
                "speak": "Sanath Jayasuriya"
            },
            {
                "question": "Which Sri Lankan cricketer is known for his unorthodox bowling action ?",
                "a": "Muttiah Muralitharan",
                "b": "Lasith Malinga",
                "c": "Ajantha Mendis",
                "d": "Sachithra Senanayake",
                "correct": "Muttiah Muralitharan",
                "speak": "Muttiah Muralitharan"
            },
            {
                "question": "Which Sri Lankan boxer won a bronze medal at the 1950 British Empire Games?",
                "a": "Duncan White",
                "b": "Eddie Gray",
                "c": "H. K. Karunaratne",
                "d": "K. P. Edwin",
                "correct": "Eddie Gray",
                "speak": "Eddie Gray"
            },
            {
                "question": "Who is the first Sri Lankan cricketer to take a hat-trick in a World Cup match?",
                "a": "Lasith Malinga",
                "b": "Chaminda Vaas",
                "c": "Ajantha Mendis",
                "d": "Nuwan Kulasekara",
                "correct": "Chaminda Vaas",
                "speak": "Chaminda Vaas"
            },
            {
                "question": "Which Sri Lankan cricketer holds the record for the most catches in Test cricket by a non-wicketkeeper?",
                "a": "Kumar Sangakkara",
                "b": "Mahela Jayawardene",
                "c": "Sanath Jayasuriya",
                "d": "Aravinda de Silva",
                "correct": "Mahela Jayawardene",
                "speak": "Mahela Jayawardene"
            },
            {
                "question": "Who is the Sri Lankan cricketer known for his distinctive slinging bowling action and is one of the greatest T20 bowlers?",
                "a": "Lasith Malinga",
                "b": "Chaminda Vaas",
                "c": "Nuwan Kulasekara",
                "d": "Thisara Perera",
                "correct": "Lasith Malinga",
                "speak": "Lasith Malinga"
            },
            {
                "question": "Which Sri Lankan athlete won the gold medal in the men’s 400m hurdles at the 1998 Asian Games?",
                "a": "Sugath Thilakaratne",
                "b": "Rohan Pradeep Kumara",
                "c": "Duncan White",
                "d": "Sriyantha Dissanayake",
                "correct": "Sugath Thilakaratne",
                "speak": "Sugath Thilakaratne"
            },
            {
                "question": "Who is the first Sri Lankan cricketer to score a double century in a Test match?",
                "a": "Sanath Jayasuriya",
                "b": "Aravinda de Silva",
                "c": "Kumar Sangakkara",
                "d": "Mahela Jayawardene",
                "correct": "Sanath Jayasuriya",
                "speak": "Sanath Jayasuriya"
            },
            {
                "question": "Which Sri Lankan cricketer is known for scoring the fastest 150 in ODI cricket?",
                "a": "Sanath Jayasuriya",
                "b": "Kumar Sangakkara",
                "c": "Tillakaratne Dilshan",
                "d": "Thisara Perera",
                "correct": "Sanath Jayasuriya",
                "speak": "Sanath Jayasuriya"
            },
            {
                "question": "Who is the first Sri Lankan female athlete to compete in the Olympics?",
                "a": "Susanthika Jayasinghe",
                "b": "Nimmi de Silva",
                "c": "Damayanthi Dharsha",
                "d": "Anuradha Cooray",
                "correct": "Damayanthi Dharsha",
                "speak": "Damayanthi Dharsha"
            },
            {
                "question": "Which Sri Lankan rugby team has won the Clifford Cup the most times?",
                "a": "Kandy SC",
                "b": "Havelock SC",
                "c": "CR & FC",
                "d": "Navy SC",
                "correct": "Kandy SC",
                "speak": "Kandy SC"
            },
            {
                "question": "Which Sri Lankan cricketer is known for his record-breaking partnership with Kumar Sangakkara in Test cricket?",
                "a": "Mahela Jayawardene",
                "b": "Sanath Jayasuriya",
                "c": "Tillakaratne Dilshan",
                "d": "Arjuna Ranatunga",
                "correct": "Mahela Jayawardene",
                "speak": "Mahela Jayawardene"
            },
            {
                "question": "Who was the captain of the Sri Lankan cricket team during the 2011 ICC Cricket World Cup?",
                "a": "Sanath Jayasuriya",
                "b": "Mahela Jayawardene",
                "c": "Kumar Sangakkara",
                "d": "Angelo Mathews",
                "correct": "Kumar Sangakkara",
                "speak": "Kumar Sangakkara"
            },
            {
                "question": "Who was the first Prime Minister of independent Sri Lanka?",
                "a": "J.R. Jayewardene",
                "b": "S.W.R.D. Bandaranaike",
                "c": "D.S. Senanayake",
                "d": "Sir John Kotelawala",
                "correct": "D.S. Senanayake",
                "speak": "D.S. Senanayake"
            },
            {
                "question": "What is the ancient name of Sri Lanka?",
                "a": "Taprobane",
                "b": "Ceylon",
                "c": "Serendib",
                "d": "Lanka",
                "correct": "Lanka",
                "speak": "Lanka"
            },
            {
                "question": "Which Sri Lankan king built the Sigiriya rock fortress?",
                "a": "King Kashyapa",
                "b": "King Dutugemunu",
                "c": "King Parakramabahu",
                "d": "King Mahasen",
                "correct": "King Kashyapa",
                "speak": "King Kashyapa"
            },
            {
                "question": "Who was the founder of the Kandyan Kingdom?",
                "a": "King Vijayabahu I",
                "b": "King Senarath",
                "c": "King Vimaladharmasuriya I",
                "d": "King Rajasinha I",
                "correct": "King Vimaladharmasuriya I",
                "speak": "King Vimaladharmasuriya I"
            },
            {
                "question": "Which colonial power first occupied Sri Lanka in the 16th century?",
                "a": "Portuguese",
                "b": "Dutch",
                "c": "British",
                "d": "French",
                "correct": "Portuguese",
                "speak": "Portuguese"
            },
            {
                "question": "Who was the last king of Sri Lanka?",
                "a": "King Rajasinghe II",
                "b": "King Buvanekabahu VI",
                "c": "King Sri Vikrama Rajasinha",
                "d": "King Dharmapala",
                "correct": "King Sri Vikrama Rajasinha",
                "speak": "King Sri Vikrama Rajasinha"
            },
            {
                "question": "In which year did Sri Lanka gain independence from British rule?",
                "a": "1948",
                "b": "1950",
                "c": "1947",
                "d": "1952",
                "correct": "1948",
                "speak": "1948"
            },
            {
                "question": "What was the ancient capital of the Anuradhapura Kingdom?",
                "a": "Kandy",
                "b": "Polonnaruwa",
                "c": "Anuradhapura",
                "d": "Sigiriya",
                "correct": "Anuradhapura",
                "speak": "Anuradhapura"
            },
            {
                "question": "Who was the leader of the JVP insurrection in 1971?",
                "a": "Rohana Wijeweera",
                "b": "Somawansa Amarasinghe",
                "c": "Wijeweera Gunaratna",
                "d": "Anura Kumara Dissanayake",
                "correct": "Rohana Wijeweera",
                "speak": "Rohana Wijeweera"
            },
            {
                "question": "Which Sri Lankan king is known for defeating the Chola invaders?",
                "a": "King Vijayabahu I",
                "b": "King Parakramabahu I",
                "c": "King Dutugemunu",
                "d": "King Buvanekabahu I",
                "correct": "King Vijayabahu I",
                "speak": "King Vijayabahu I"
            },
            {
                "question": "Which kingdom was established in the south of Sri Lanka and resisted European colonization?",
                "a": "Anuradhapura",
                "b": "Polonnaruwa",
                "c": "Jaffna",
                "d": "Kandy",
                "correct": "Kandy",
                "speak": "Kandy"
            },
            {
                "question": "Who was the first President of Sri Lanka?",
                "a": "Ranasinghe Premadasa",
                "b": "William Gopallawa",
                "c": "J.R. Jayewardene",
                "d": "S.W.R.D. Bandaranaike",
                "correct": "J.R. Jayewardene",
                "speak": "J.R. Jayewardene"
            },
            {
                "question": "Which king is famous for the construction of the Parakrama Samudra?",
                "a": "King Vijayabahu I",
                "b": "King Dutugemunu",
                "c": "King Parakramabahu I",
                "d": "King Buvanekabahu I",
                "correct": "King Parakramabahu I",
                "speak": "King Parakramabahu I"
            },
            {
                "question": "What is the ancient name of Anuradhapura?",
                "a": "Tambapanni",
                "b": "Upatissa",
                "c": "Anura",
                "d": "Mahagama",
                "correct": "Upatissa",
                "speak": "Upatissa"
            },
            {
                "question": "Who was the first Sinhala king to rule Sri Lanka?",
                "a": "King Vijaya",
                "b": "King Pandukabhaya",
                "c": "King Devanampiya Tissa",
                "d": "King Dutugemunu",
                "correct": "King Vijaya",
                "speak": "King Vijaya"
            },
            {
                "question": "Which Sri Lankan city was known as the 'Granary of the East'?",
                "a": "Anuradhapura",
                "b": "Polonnaruwa",
                "c": "Kandy",
                "d": "Galle",
                "correct": "Polonnaruwa",
                "speak": "Polonnaruwa"
            },
            {
                "question": "Who was the founder of the Jaffna Kingdom?",
                "a": "King Sangili",
                "b": "King Kalinga Magha",
                "c": "King Aryacakravarti",
                "d": "King Pararajasekaram",
                "correct": "King Aryacakravarti",
                "speak": "King Aryacakravarti"
            },
            {
                "question": "Which Sri Lankan king is known for his efforts to restore Buddhism in the country?",
                "a": "King Dutugemunu",
                "b": "King Vijayabahu I",
                "c": "King Devanampiya Tissa",
                "d": "King Parakramabahu I",
                "correct": "King Devanampiya Tissa",
                "speak": "King Devanampiya Tissa"
            },
            {
                "question": "Which European country took control of Sri Lanka from the Portuguese in 1658?",
                "a": "France",
                "b": "Netherlands",
                "c": "Spain",
                "d": "Denmark",
                "correct": "Netherlands",
                "speak": "Netherlands"
            },
            {
                "question": "Who was the first female Prime Minister of Sri Lanka?",
                "a": "Sirimavo Bandaranaike",
                "b": "Chandrika Kumaratunga",
                "c": "Indira Gandhi",
                "d": "Margaret Thatcher",
                "correct": "Sirimavo Bandaranaike",
                "speak": "Sirimavo Bandaranaike"
            },
            {
                "question": "Which ancient Sri Lankan kingdom is known for its elaborate irrigation systems?",
                "a": "Kandy",
                "b": "Anuradhapura",
                "c": "Gampola",
                "d": "Jaffna",
                "correct": "Anuradhapura",
                "speak": "Anuradhapura"
            },
            {
                "question": "Who was the first Governor-General of independent Sri Lanka?",
                "a": "William Gopallawa",
                "b": "D.S. Senanayake",
                "c": "Sir Oliver Goonetilleke",
                "d": "Sir John Kotelawala",
                "correct": "Sir Oliver Goonetilleke",
                "speak": "Sir Oliver Goonetilleke"
            },
            {
                "question": "Which Sri Lankan kingdom was known for its resistance against Portuguese colonization?",
                "a": "Kandy",
                "b": "Anuradhapura",
                "c": "Polonnaruwa",
                "d": "Jaffna",
                "correct": "Kandy",
                "speak": "Kandy"
            },
            {
                "question": "Who was the first Sinhalese king to convert to Buddhism?",
                "a": "King Vijaya",
                "b": "King Pandukabhaya",
                "c": "King Devanampiya Tissa",
                "d": "King Dutugemunu",
                "correct": "King Devanampiya Tissa",
                "speak": "King Devanampiya Tissa"
            },
            {
                "question": "What was the main export of ancient Sri Lanka that attracted European colonizers?",
                "a": "Spices",
                "b": "Gold",
                "c": "Silk",
                "d": "Tea",
                "correct": "Spices",
                "speak": "Spices"
            },
            {
                "question": "Who was the leader of the Sri Lankan independence movement?",
                "a": "S.W.R.D. Bandaranaike",
                "b": "D.S. Senanayake",
                "c": "Ranasinghe Premadasa",
                "d": "J.R. Jayewardene",
                "correct": "D.S. Senanayake",
                "speak": "D.S. Senanayake"
            },
            {
                "question": "Which ancient city in Sri Lanka is a UNESCO World Heritage Site known for its well-preserved ruins?",
                "a": "Kandy",
                "b": "Polonnaruwa",
                "c": "Jaffna",
                "d": "Colombo",
                "correct": "Polonnaruwa",
                "speak": "Polonnaruwa"
            },
            {
                "question": "Who is known as the father of modern medicine in Sri Lanka?",
                "a": "Dr. S. R. Kottegoda",
                "b": "Dr. C. G. Uragoda",
                "c": "Dr. P. B. Fernando",
                "d": "Dr. A. R. Perera",
                "correct": "Dr. P. B. Fernando",
                "speak": "Dr. P. B. Fernando"
            },
            {
                "question": "Which Sri Lankan scientist is renowned for his work in the field of chemistry and was awarded the Vidya Jyothi title?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. R. O. B. Wijesekera",
                "speak": "Prof. R. O. B. Wijesekera"
            },
            {
                "question": "Who is a well-known Sri Lankan astrophysicist noted for his contributions to the theory of panspermia?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan physicist is famous for his research in environmental physics and sustainable development?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Mohan Munasinghe",
                "speak": "Prof. Mohan Munasinghe"
            },
            {
                "question": "Who discovered the SARS coronavirus and is a leading virologist in Sri Lanka?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Malik Peiris",
                "speak": "Prof. Malik Peiris"
            },
            {
                "question": "Which Sri Lankan botanist is known for his work on the flora of Sri Lanka and the South Asian region?",
                "a": "Dr. S. R. Kottegoda",
                "b": "Dr. C. G. Uragoda",
                "c": "Dr. P. B. Fernando",
                "d": "Dr. A. R. Perera",
                "correct": "Dr. C. G. Uragoda",
                "speak": "Dr. C. G. Uragoda"
            },
            {
                "question": "Who was the first Sri Lankan to be elected as a Fellow of the Royal Society?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Chandra Wickramasinghe",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Malik Peiris",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan engineer is known for his contributions to water resources management and hydrology?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Mohan Munasinghe",
                "c": "Prof. Chandra Wickramasinghe",
                "d": "Prof. A. W. Jayawardene",
                "correct": "Prof. A. W. Jayawardene",
                "speak": "Prof. A. W. Jayawardene"
            },
            {
                "question": "Who is a pioneering Sri Lankan scientist in the field of space science and satellite technology?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan scientist is known for his work on the epidemiology of infectious diseases?",
                "a": "Prof. Malik Peiris",
                "b": "Prof. R. O. B. Wijesekera",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Malik Peiris",
                "speak": "Prof. Malik Peiris"
            },
            {
                "question": "Who is the Sri Lankan physicist awarded the Nobel Prize in Physics in 2021?",
                "a": "Prof. Chandra Wickramasinghe",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. R. O. B. Wijesekera",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan biologist is known for his research on the biodiversity of Sri Lanka?",
                "a": "Dr. S. R. Kottegoda",
                "b": "Dr. C. G. Uragoda",
                "c": "Dr. P. B. Fernando",
                "d": "Dr. A. R. Perera",
                "correct": "Dr. S. R. Kottegoda",
                "speak": "Dr. S. R. Kottegoda"
            },
            {
                "question": "Who is a prominent Sri Lankan scientist in the field of agricultural science?",
                "a": "Dr. W. D. Ratnasooriya",
                "b": "Dr. S. R. Kottegoda",
                "c": "Dr. P. B. Fernando",
                "d": "Dr. A. R. Perera",
                "correct": "Dr. W. D. Ratnasooriya",
                "speak": "Dr. W. D. Ratnasooriya"
            },
            {
                "question": "Which Sri Lankan scientist made significant contributions to the study of marine biology?",
                "a": "Dr. S. R. Kottegoda",
                "b": "Dr. C. G. Uragoda",
                "c": "Dr. P. B. Fernando",
                "d": "Dr. A. R. Perera",
                "correct": "Dr. A. R. Perera",
                "speak": "Dr. A. R. Perera"
            },
            {
                "question": "Who is the Sri Lankan chemist known for his work on natural products and medicinal chemistry?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. R. O. B. Wijesekera",
                "speak": "Prof. R. O. B. Wijesekera"
            },
            {
                "question": "Which Sri Lankan scientist is renowned for his work in climate change and environmental science?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Mohan Munasinghe",
                "speak": "Prof. Mohan Munasinghe"
            },
            {
                "question": "Who is a leading Sri Lankan researcher in the field of immunology?",
                "a": "Prof. Malik Peiris",
                "b": "Prof. R. O. B. Wijesekera",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Malik Peiris",
                "speak": "Prof. Malik Peiris"
            },
            {
                "question": "Which Sri Lankan scientist has made significant contributions to the field of nanotechnology?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Who is the Sri Lankan physicist known for his research on quantum mechanics?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Chandra Wickramasinghe",
                "speak": "Prof. Chandra Wickramasinghe"
            },
            {
                "question": "Which Sri Lankan scientist is noted for his work on tropical diseases?",
                "a": "Prof. Malik Peiris",
                "b": "Prof. R. O. B. Wijesekera",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Malik Peiris",
                "speak": "Prof. Malik Peiris"
            },
            {
                "question": "Who is a renowned Sri Lankan scientist in the field of genetics?",
                "a": "Prof. R. O. B. Wijesekera",
                "b": "Prof. Malik Peiris",
                "c": "Prof. Mohan Munasinghe",
                "d": "Prof. Chandra Wickramasinghe",
                "correct": "Prof. Malik Peiris",
                "speak": "Prof. Malik Peiris"
            }
        ]
    else:
        questionArray = [
            {
                "question": "'Starry Night' සිතුවම් කළේ කවුද?",
                "a": "පැබ්ලෝ පිකාසෝ",
                "b": "ලියනාඩෝ ඩා වින්චි",
                "c": "වින්සන්ට් වැන් ගොග්",
                "d": "ක්ලෝඩ් මොනේට්",
                "correct": "වින්සන්ට් වැන් ගොග්",
                "speak": "winsent van gog"
            },
            {
                "question": "මිනිස් සිරුරේ කුඩාම අස්ථිය කුමක්ද?",
                "a": "ස්ටේප්ස්",
                "b": "Femur",
                "c": "ටිබියා",
                "d": "ෆයිබුලා",
                "correct": "ස්ටේප්ස්",
                "speak": "steps"
            },
            {
                "question": "'To Kill a Mockingbird' ලිව්වේ කවුද?",
                "a": "හාපර් ලී",
                "b": "මාර්ක් ට්වේන්",
                "c": "F. ස්කොට් ෆිට්ස්ගේරාල්",
                "d": "අර්නස්ට් හෙමිංවේ",
                "correct": "හාපර් ලී",
                "speak": "harper lee"
            },
            {
                "question": "සෝඩියම් සඳහා රසායනික සංකේතය කුමක්ද?",
                "a": "So",
                "b": "Sa",
                "c": "N",
                "d": "Na",
                "correct": "Na",
                "speak": "N A"
            },
            {
                "question": "සාපේක්ෂතාවාදයේ න්‍යාය හදුන්වා දුන්නේ කවුද?",
                "a": "අයිසැක් නිව්ටන්",
                "b": "ගැලීලියෝ ගැලීලි",
                "c": "ඇල්බට් අයින්ස්ටයින්",
                "d": "නීල්ස් බෝර්",
                "correct": "ඇල්බට් අයින්ස්ටයින්",
                "speak": "albert aistain"
            },
            {
                "question": "'නිල් ග්‍රහලෝකය' ලෙස හඳුන්වන්නේ කුමන ග්‍රහලෝකයද?",
                "a": "අඟහරු",
                "b": "පෘථුවිය",
                "c": "නෙප්චූන්",
                "d": "යුරේනස්",
                "correct": "පෘථුවිය",
                "speak": "pruthuwiya"
            },
            {
                "question": "ලෝකයේ උසම ගොඩනැගිල්ල කුමක්ද?",
                "a": "ෂැංහයි කුළුණ",
                "b": "Abraj Al-Bait",
                "c": "බර්ජ් කලීෆා",
                "d": "ලෝක වෙළඳ මධ්‍යස්ථානය",
                "correct": "බර්ජ් කලීෆා",
                "speak": "burj kalifha"
            },
            {
                "question": "ජපානයේ මුදල් ඒකකය කුමක්ද?",
                "a": "Yuan",
                "b": "Won",
                "c": "Yen",
                "d": "Dollar",
                "correct": "Yen",
                "speak": "Yen"
            },
            {
                "question": "දුරකථනය සොයාගත්තේ කවුද?",
                "a": "තෝමස් එඩිසන්",
                "b": "නිකොලා ටෙස්ලා",
                "c": "ඇලෙක්සැන්ඩර් ග්රැහැම් බෙල්",
                "d": "ගුග්ලියෙල්මෝ මාකෝනි",
                "correct": "ඇලෙක්සැන්ඩර් ග්රැහැම් බෙල්",
                "speak": "alexander graham bell"
            },
            {
                "question": "ලෝකයේ කුඩාම රට කුමක්ද?",
                "a": "මොනාකෝ",
                "b": "සැන් මරිනෝ",
                "c": "වතිකානු",
                "d": "ලිච්ටෙන්ස්ටයින්",
                "correct": "වතිකානු",
                "speak": "wathikanuwa"
            },
            {
                "question": "විශාලතම සාගරය කුමක්ද?",
                "a": "අත්ලාන්තික් සාගරය",
                "b": "ඉන්දියන් සාගරය",
                "c": "ආක්ටික් සාගරය",
                "d": "ශාන්තිකර සාගරය",
                "correct": "ශාන්තිකර සාගරය",
                "speak": "shanthikara sagaraya"
            },
            {
                "question": "මොනාලිසා සිතුවම් කළේ කවුද?",
                "a": "ලියනාඩෝ ඩා වින්චි",
                "b": "වින්සන්ට් වැන් ගොග්",
                "c": "පැබ්ලෝ පිකාසෝ",
                "d": "ක්ලෝඩ් මොනේට්",
                "correct": "ලියනාඩෝ ඩා වින්චි",
                "speak": "liyanado da winchi"
            },
            {
                "question": "'Pride and Prejudice' ලිව්වේ කවුද?",
                "a": "ජේන් ඔස්ටින්",
                "b": "චාලට් බ්‍රොන්ටේ",
                "c": "එමිලි බ්‍රොන්ටේ",
                "d": "ජෝර්ජ් එලියට්",
                "correct": "ජේන් ඔස්ටින්",
                "speak": "jen ostin"
            },
            {
                "question": "ලෝකයේ උසම කන්ද කුමක්ද?",
                "a": "K2",
                "b": "එවරස්ට් කන්ද",
                "c": "කන්චෙන්ජුංගා",
                "d": "ලොට්සේ",
                "correct": "එවරස්ට් කන්ද",
                "speak": "ewarast kanda"
            },
            {
                "question": "අපේ සෞරග්‍රහ මණ්ඩලයේ කුඩාම ග්‍රහලෝකය කුමක්ද?",
                "a": "අඟහරු",
                "b": "සිකුරු",
                "c": "බුධ",
                "d": "ප්ලූටෝ",
                "correct": "බුධ",
                "speak": "budha"
            },
            {
                "question": "විශාලතම මහාද්වීපය කුමක්ද?",
                "a": "අප්‍රිකාව",
                "b": "ආසියාව",
                "c": "යුරෝපය",
                "d": "උතුරු ඇමෙරිකාව",
                "correct": "ආසියාව",
                "speak": "asiyawa"
            },
            {
                "question": "පෝලියෝ එන්නත නිපදවූයේ කවුද?",
                "a": "ඇල්බට් සබින්",
                "b": "ලුවී පාස්චර්",
                "c": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
                "d": "ජෝනාස් සල්ක්",
                "correct": "ජෝනාස් සල්ක්",
                "speak": "jonas salk"
            },
            {
                "question": "බ්‍රසීලයේ කතා කරන මූලික භාෂාව කුමක්ද?",
                "a": "ස්පාඤ්ඤ",
                "b": "පෘතුගීසි",
                "c": "ඉංග්රීසි",
                "d": "ප්‍රංශ",
                "correct": "පෘතුගීසි",
                "speak": "pruthugisi"
            },
            {
                "question": "'O' රසායනික සංකේතය ඇති මූලද්‍රව්‍ය මොනවාද?",
                "a": "ඔස්මියම්",
                "b": "ඔක්සිජන්",
                "c": "ඔගනෙසන්",
                "d": "ඔක්සලේට්",
                "correct": "ඔක්සිජන්",
                "speak": "oxigen"
            },
            {
                "question": "1912 දී ගිලී ගිය සුප්‍රසිද්ධ නෞකාව කුමක්ද?",
                "a": "ලුසිටානියා",
                "b": "බ්‍රිටැනික්",
                "c": "ටයිටැනික්",
                "d": "මේරි රැජින",
                "correct": "ටයිටැනික්",
                "speak": "titanic"
            },
            {
                "question": "ලෝකයේ විශාලතම ක්ෂීරපායී සත්වයා කුමක්ද?",
                "a": "අප්රිකානු අලියා",
                "b": "නිල් තල්මසා",
                "c": "ජිරාෆ්",
                "d": "මහා සුදු මෝරා",
                "correct": "නිල් තල්මසා",
                "speak": "nil thalmasa"
            },
            {
                "question": "'හැම්ලට්' ලිව්වේ කවුද?",
                "a": "චාර්ල්ස් ඩිකන්ස්",
                "b": "ජේන් ඔස්ටින්",
                "c": "විලියම් ශේක්ස්පියර්",
                "d": "මාර්ක් ට්වේන්",
                "correct": "විලියම් ශේක්ස්පියර්",
                "speak": "wiliyan shekspiyar"
            },
            {
                "question": "සූර්යයාගේ ප්රධාන සංරචකය කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "හයිඩ්රජන්",
                "c": "කාබන්",
                "d": "හීලියම්",
                "correct": "හයිඩ්රජන්",
                "speak": "haigragen"
            },
            {
                "question": "චීනයේ අගනුවර කුමක්ද?",
                "a": "ෂැංහයි",
                "b": "බීජිං",
                "c": "හොංකොං",
                "d": "චෙන්ග්ඩු",
                "correct": "බීජිං",
                "speak": "beejin"
            },
            {
                "question": "පෘථිවි වායුගෝලයේ ඇති ප්‍රාථමික වායුව කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "කාබන් ඩයොක්සයිඩ්",
                "c": "නයිට්රජන්",
                "d": "හයිඩ්රජන්",
                "correct": "නයිට්රජන්",
                "speak": "naitragen"
            },
            {
                "question": "සිස්ටයින් දේවස්ථානයේ සිවිලිම පින්තාරු කළේ කවුද?",
                "a": "ලියනාඩෝ ඩා වින්චි",
                "b": "රෆායෙල්",
                "c": "මයිකල් ඇන්ජලෝ",
                "d": "ඩොනෙටෙලෝ",
                "correct": "මයිකල් ඇන්ජලෝ",
                "speak": "micel angelo"
            },
            {
                "question": "ලෝකයේ උසම සත්වයා කුමක්ද?",
                "a": "අලියා",
                "b": "නිල් තල්මසා",
                "c": "ජිරාෆ්",
                "d": "මහා සුදු මෝරා",
                "correct": "ජිරාෆ්",
                "speak": "jiraf"
            },
            {
                "question": "ලෝකයේ වැඩිපුරම කතා කරන භාෂාව කුමක්ද?",
                "a": "ස්පාඤ්ඤ",
                "b": "ඉංග්රීසි",
                "c": "මැන්ඩරින්",
                "d": "හින්දි",
                "correct": "මැන්ඩරින්",
                "speak": "manderin"
            },
            {
                "question": "ඉන්දියාවේ මුදල් ඒකකය යනු කුමක්ද?",
                "a": "රුපියල",
                "b": "ටකා",
                "c": "රියාල්",
                "d": "යෙන්",
                "correct": "රුපියල",
                "speak": "rupiyala"
            },
            {
                "question": "ලෝකයේ උසම දිය ඇල්ල කුමක්ද?",
                "a": "නයගරා ඇල්ල",
                "b": "ඒන්ජල් ඇල්ල",
                "c": "වික්ටෝරියා දිය ඇල්ල",
                "d": "ඉගුවාසු ඇල්ල",
                "correct": "ඒන්ජල් ඇල්ල",
                "speak": "angel ella"
            },
            {
                "question": "'රතු ග්‍රහලෝකය' ලෙස හඳුන්වන්නේ කුමන ග්‍රහලෝකයද?",
                "a": "බ්‍රහස්පති",
                "b": "අඟහරු",
                "c": "සෙනසුරු",
                "d": "නෙප්චූන්",
                "correct": "අඟහරු",
                "speak": "agaharu"
            },
            {
                "question": "'The Divine Comedy' ලිව්වේ කවුද?",
                "a": "Dante Alighieri",
                "b": "ජෙෆ්රි චෞසර්",
                "c": "විලියම් බ්ලේක්",
                "d": "ජෝන් මිල්ටන්",
                "correct": "Dante Alighieri",
                "speak": "Dante Alighieri"
            },
            {
                "question": "ජර්මනියේ අගනුවර කුමක්ද?",
                "a": "මියුනිච්",
                "b": "ෆ්රෑන්ක්ෆර්ට්",
                "c": "බර්ලින්",
                "d": "හැම්බර්ග්",
                "correct": "බර්ලින්",
                "speak": "berlin"
            },
            {
                "question": "The Great Gatsby කෘතියේ කතුවරයා කවුද?",
                "a": "අර්නස්ට් හෙමිංවේ",
                "b": "JD Salinger",
                "c": "F. Scott Fitzgerald",
                "d": "ජෝන් ස්ටයින්බෙක්",
                "correct": "F. Scott Fitzgerald",
                "speak": "F. Scott Fitzgerald"
            },
            {
                "question": "චීනයේ මුදල් ඒකකය කුමක්ද?",
                "a": "Yen",
                "b": "Won",
                "c": "Yuan",
                "d": "Rupee",
                "correct": "Yuan",
                "speak": "Yuan"
            },
            {
                "question": "පරිගණනයේ පියා ලෙස හඳුන්වන්නේ කවුද?",
                "a": "ඇලන් ටියුරින්",
                "b": "චාල්ස් බැබේජ්",
                "c": "ජෝන් වොන් නියුමන්",
                "d": "බිල් ගේට්ස්",
                "correct": "චාල්ස් බැබේජ්",
                "speak": "charls babej"
            },
            {
                "question": "'HTTP' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "HyperText Transmission Protocol",
                "b": "Hyper Transfer Text Protocol",
                "c": "Hyper Transmission Text Protocol",
                "d": "HyperText Transfer Protocol",
                "correct": "HyperText Transfer Protocol",
                "speak": "HyperText Transfer Protocol"
            },
            {
                "question": "'World Wide Web' සොයාගත්තේ කවුද?",
                "a": "ටිම් බර්නර්ස්-ලී",
                "b": "බිල් ගේට්ස්",
                "c": "ස්ටීව් ජොබ්ස්",
                "d": "මාර්ක් සකර්බර්ග්",
                "correct": "ටිම් බර්නර්ස්-ලී",
                "speak": "tim bernes lee"
            },
            {
                "question": "පරිගණකවල 'CPU' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Central Processing Unit",
                "b": "Central Power Unit",
                "c": "Central Programming Unit",
                "d": "Central Print Unit",
                "correct": "Central Processing Unit",
                "speak": "Central Processing Unit"
            },
            {
                "question": "Android මෙහෙයුම් පද්ධතිය නිපදවූ සමාගම කුමක්ද?",
                "a": "ඇපල්",
                "b": "Microsoft",
                "c": "ගූගල්",
                "d": "සැම්සුන්",
                "correct": "ගූගල්",
                "speak": "google"
            },
            {
                "question": "'RAM' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Random Access Memory",
                "b": "Read Access Memory",
                "c": "Read-Only Memory",
                "d": "Randomly Allocated Memory",
                "correct": "Random Access Memory",
                "speak": "Random Access Memory"
            },
            {
                "question": "පළමු ඉලෙක්ට්‍රොනික පොදු කාර්ය පරිගණකයේ නම කුමක්ද?",
                "a": "UNIVAC",
                "b": "ENIAC",
                "c": "EDVAC",
                "d": "IBM 701",
                "correct": "ENIAC",
                "speak": "ENIAC"
            },
            {
                "question": "පළමු චිත්‍රක වෙබ් බ්‍රව්සරයේ නම කුමක්ද?",
                "a": "Internet Explorer",
                "b": "Netscape Navigator",
                "c": "Mosaic",
                "d": "Opera",
                "correct": "Mosaic",
                "speak": "Mosaic"
            },
            {
                "question": "Microsoft හි Cloud computing සේවාවේ නම කුමක්ද?",
                "a": "Azure",
                "b": "AWS",
                "c": "Google Cloud",
                "d": "IBM Cloud",
                "correct": "Azure",
                "speak": "Azure"
            },
            {
                "question": "බිල් ගේට්ස් සමඟ එක්ව මයික්‍රොසොෆ්ට් ආරම්භ කළේ කවුද?",
                "a": "ස්ටීව් වොස්නියැක්",
                "b": "පෝල් ඇලන්",
                "c": "ලැරී පේජ්",
                "d": "සර්ජි බ්‍රින්",
                "correct": "පෝල් ඇලන්",
                "speak": "pol alen"
            },
            {
                "question": "වෙබ් භාෂාව ලෙස හඳුන්වන ක්‍රමලේඛන භාෂාව කුමක්ද?",
                "a": "Python",
                "b": "Java",
                "c": "C++",
                "d": "JavaScript",
                "correct": "JavaScript",
                "speak": "JavaScript"
            },
            {
                "question": "'URL' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Uniform Resource Locator",
                "b": "Uniform Reference Locator",
                "c": "Universal Resource Locator",
                "d": "Universal Reference Locator",
                "correct": "Uniform Resource Locator",
                "speak": "Uniform Resource Locator"
            },
            {
                "question": "'ThinkPad' ලැප්ටොප් පෙළ සඳහා ප්‍රසිද්ධ සමාගම කුමක්ද?",
                "a": "ඇපල්",
                "b": "එච්.පී",
                "c": "ඩෙල්",
                "d": "ලෙනොවෝ",
                "correct": "ලෙනොවෝ",
                "speak": "lenovo"
            },
            {
                "question": "'PDF' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Portable Document Format",
                "b": "Public Document Format",
                "c": "Portable Data Format",
                "d": "Public Data Format",
                "correct": "Portable Document Format",
                "speak": "Portable Document Format"
            },
            {
                "question": "පළමු මයික්‍රොප්‍රොසෙසරය නිපදවූ සමාගම කුමක්ද?",
                "a": "ඉන්ටෙල්",
                "b": "AMD",
                "c": "IBM",
                "d": "ටෙක්සාස් උපකරණ",
                "correct": "ඉන්ටෙල්",
                "speak": "intel"
            },
            {
                "question": "2021 වන විට වඩාත්ම ජනප්‍රිය ක්‍රමලේඛන භාෂාව කුමක්ද?",
                "a": "Python",
                "b": "JavaScript",
                "c": "Java",
                "d": "C++",
                "correct": "Python",
                "speak": "Python"
            },
            {
                "question": "වින්ඩෝස් හි පළමු අනුවාදය නිකුත් කළේ කුමන වසරේද?",
                "a": "1983",
                "b": "1984",
                "c": "1985",
                "d": "1986",
                "correct": "1985",
                "speak": "ekdahas nawasiya asupaha"
            },
            {
                "question": "පරිගණක ගබඩා කිරීමේදී 'SSD' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Solid State Drive",
                "b": "Secure Storage Device",
                "c": "Solid Storage Drive",
                "d": "Secure State Drive",
                "correct": "Solid State Drive",
                "speak": "Solid State Drive"
            },
            {
                "question": "එහි GeForce ග්‍රැෆික් කාඩ්පත් සඳහා ප්‍රසිද්ධ සමාගම කුමක්ද?",
                "a": "AMD",
                "b": "ඉන්ටෙල්",
                "c": "NVIDIA",
                "d": "ASUS",
                "correct": "NVIDIA",
                "speak": "NVIDIA"
            },
            {
                "question": "Apple හි desktop මෙහෙයුම් පද්ධතියේ නම කුමක්ද?",
                "a": "iOS",
                "b": "macOS",
                "c": "වින්ඩෝස්",
                "d": "ලිනක්ස්",
                "correct": "macOS",
                "speak": "mac O S"
            },
            {
                "question": "PlayStation gaming console නිර්මාණය කළේ කුමන සමාගමද?",
                "a": "Microsoft",
                "b": "නින්ටෙන්ඩෝ",
                "c": "Sony",
                "d": "සේගා",
                "correct": "Sony",
                "speak": "Sony"
            },
            {
                "question": "'LAN' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Local Area Network",
                "b": "Large Area Network",
                "c": "Long Area Network",
                "d": "Limited Area Network",
                "correct": "Local Area Network",
                "speak": "Local Area Network"
            },
            {
                "question": "මාර්ක් සකර්බර්ග් විසින් ආරම්භ කරන ලද සමාජ මාධ්‍ය වේදිකාව කුමක්ද?",
                "a": "ට්විටර්",
                "b": "Instagram",
                "c": "LinkedIn",
                "d": "ෆේස්බුක්",
                "correct": "ෆේස්බුක්",
                "speak": "facebook"
            },
            {
                "question": "iOS සංවර්ධනය සඳහා මූලික වශයෙන් භාවිතා කරන ක්‍රමලේඛන භාෂාව කුමක්ද?",
                "a": "Java",
                "b": "Swift",
                "c": "C#",
                "d": "Ruby",
                "correct": "Swift",
                "speak": "Swift"
            },
            {
                "question": "'VPN' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Virtual Private Network",
                "b": "Virtual Public Network",
                "c": "Virtual Protected Network",
                "d": "Virtual Personal Network",
                "correct": "Virtual Private Network",
                "speak": "Virtual Private Network"
            },
            {
                "question": "ලිනක්ස් මෙහෙයුම් පද්ධතිය නිපදවූ සමාගම කුමක්ද?",
                "a": "IBM",
                "b": "Microsoft",
                "c": "Red Hat",
                "d": "ඉහත කිසිවක් නොවේ",
                "correct": "ඉහත කිසිවක් නොවේ",
                "speak": "ihatha kisiwak nowe"
            },
            {
                "question": "YouTube ආරම්භ කළේ කුමන වසරේද?",
                "a": "2003",
                "b": "2004",
                "c": "2005",
                "d": "2006",
                "correct": "2005",
                "speak": "dedahas paha"
            },
            {
                "question": "'IoT' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Internet of Things",
                "b": "Internet of Technology",
                "c": "Internet of Tools",
                "d": "Internet of Transactions",
                "correct": "Internet of Things",
                "speak": "Internet of Things"
            },
            {
                "question": "Surface ටැබ්ලට් පෙළ නිෂ්පාදනය කරන්නේ කුමන සමාගමද?",
                "a": "ඇපල්",
                "b": "සැම්සුන්",
                "c": "Microsoft",
                "d": "ගූගල්",
                "correct": "Microsoft",
                "speak": "Microsoft"
            },
            {
                "question": "'AI' යන්නෙන් අදහස් කරන්නේ කුමක්ද?",
                "a": "Automated Intelligence",
                "b": "Artificial Intelligence",
                "c": "Actual Intelligence",
                "d": "Augmented Intelligence",
                "correct": "Artificial Intelligence",
                "speak": "Artificial Intelligence"
            },
            {
                "question": "2021 වන විට ටෙස්ලා හි ප්‍රධාන විධායක නිලධාරියා කවුද?",
                "a": "ජෙෆ් බෙසෝස්",
                "b": "ටිම් කුක්",
                "c": "එලොන් මස්ක්",
                "d": "සුන්දර් පිචායි",
                "correct": "එලොන් මස්ක්",
                "speak": "elon musk"
            },
            {
                "question": "එක්සත් ජනපදයේ පළමු ජනාධිපති කවුද?",
                "a": "ජෝර්ජ් වොෂින්ටන්",
                "b": "තෝමස් ජෙෆර්සන්",
                "c": "ජෝන් ඇඩම්ස්",
                "d": "ජේම්ස් මැඩිසන්",
                "correct": "ජෝර්ජ් වොෂින්ටන්",
                "speak": "jorj woshington"
            },
            {
                "question": "දෙවන ලෝක යුද්ධය අවසන් වූයේ කුමන වසරේද?",
                "a": "1943",
                "b": "1944",
                "c": "1945",
                "d": "1946",
                "correct": "1945",
                "speak": "ekdahan nawasiya hathalis paha"
            },
            {
                "question": "යකඩ ගැහැනිය ලෙස හැඳින්වූයේ කවුද?",
                "a": "ඇන්ජෙලා මර්කල්",
                "b": "ඉන්දිරා ගාන්ධි",
                "c": "මාග්රට් තැචර්",
                "d": "ගෝල්ඩා මීර්",
                "correct": "මාග්රට් තැචර්",
                "speak": "magret thacher"
            },
            {
                "question": "ඇමරිකාව සොයාගත්තේ කවුද?",
                "a": "මාර්කෝ පෝලෝ",
                "b": "ෆර්ඩිනන්ඩ් මැගෙලන්",
                "c": "ක්‍රිස්ටෝපර් කොලම්බස්",
                "d": "වාස්කෝ ද ගාමා",
                "correct": "ක්‍රිස්ටෝපර් කොලම්බස්",
                "speak": "kristoper kolombus"
            },
            {
                "question": "ප්‍රංශ විප්ලවය ආරම්භ වූයේ කුමන වසරේද?",
                "a": "1776",
                "b": "1789",
                "c": "1799",
                "d": "1804",
                "correct": "1789",
                "speak": "ekdahan hathsiya asu nawaye"
            },
            {
                "question": "සඳ මත පා තැබූ පළමු මිනිසා කවුද?",
                "a": "Buzz Aldrin",
                "b": "යූරි ගගාරින්",
                "c": "ජෝන් ග්ලෙන්",
                "d": "නීල් ආම්ස්ට්‍රෝං",
                "correct": "නීල් ආම්ස්ට්‍රෝං",
                "speak": "neel amestron"
            },
            {
                "question": "පිරමිඩ ඉදිකළ පැරණි ශිෂ්ටාචාරය කුමක්ද?",
                "a": "රෝම",
                "b": "ග්‍රීක",
                "c": "ඊජිප්තු",
                "d": "මායන්",
                "correct": "ඊජිප්තු",
                "speak": "egipthu"
            },
            {
                "question": "'Declaration of Independence' ප්‍රධාන කතුවරයා කවුද?",
                "a": "ජෝන් ඇඩම්ස්",
                "b": "බෙන්ජමින් ෆ්රෑන්ක්ලින්",
                "c": "තෝමස් ජෙෆර්සන්",
                "d": "ජේම්ස් මැඩිසන්",
                "correct": "තෝමස් ජෙෆර්සන්",
                "speak": "thomas jeferson"
            },
            {
                "question": "ඇමරිකානු සිවිල් යුද්ධයේ මූලික හේතුව කුමක්ද?",
                "a": "ආර්ථික වෙනස්කම්",
                "b": "වහල්භාවය",
                "c": "භෞමික ව්යාප්තිය",
                "d": "දේශපාලන පක්ෂ",
                "correct": "වහල්භාවය",
                "speak": "wahalbhawaya"
            },
            {
                "question": "දෙවන එලිසබෙත් රැජිනට පෙර දීර්ඝතම කාලයක් පාලනය කළ බ්‍රිතාන්‍ය රජ කවුද?",
                "a": "වික්ටෝරියා රැජින",
                "b": "III ජෝර්ජ් රජු",
                "c": "මේරි රැජින I",
                "d": "I එලිසබෙත් රැජින",
                "correct": "වික්ටෝරියා රැජින",
                "speak": "wiktoriya rajina"
            },
            {
                "question": "ජෙන්ගිස් ඛාන් පිහිටුවූ අධිරාජ්‍යය කුමක්ද?",
                "a": "රෝම අධිරාජ්‍යය",
                "b": "මොන්ගෝලියානු අධිරාජ්‍යය",
                "c": "ඔටෝමන් අධිරාජ්‍යය",
                "d": "පර්සියානු අධිරාජ්යය",
                "correct": "මොන්ගෝලියානු අධිරාජ්‍යය",
                "speak": "mongoliyanu adhirajya"
            },
            {
                "question": "බර්ලින් තාප්පය කඩා දැමුවේ කුමන වසරේද?",
                "a": "1987",
                "b": "1988",
                "c": "1989",
                "d": "1990",
                "correct": "1989",
                "speak": "ekdahas nawasiya asu nawaya"
            },
            {
                "question": "එක්සත් රාජධානියේ පළමු කාන්තා අගමැතිනිය කවුද?",
                "a": "මාග්රට් තැචර්",
                "b": "තෙරේසා මේ",
                "c": "ඉන්දිරා ගාන්ධි",
                "d": "ඇන්ජෙලා මර්කල්",
                "correct": "මාග්රට් තැචර්",
                "speak": "magret thacher"
            },
            {
                "question": "1963 නොවැම්බර් 22 ඝාතනය කළේ කවුද?",
                "a": "මාටින් ලූතර් කිං ජූනියර්",
                "b": "රොබට් එෆ් කෙනඩි",
                "c": "ජෝන් එෆ් කෙනඩි",
                "d": "මැල්කම් එක්ස්",
                "correct": "ජෝන් එෆ් කෙනඩි",
                "speak": "jhon f kenedy"
            },
            {
                "question": "එක්සත් ජනපදයේ උතුරු සහ දකුණු ප්‍රදේශ අතර ඇති වූ යුද්ධය කුමක්ද?",
                "a": "පළමු ලෝක යුද්ධය",
                "b": "දෙවන ලෝක යුද්ධය",
                "c": "සිවිල් යුද්ධය",
                "d": "විප්ලවවාදී යුද්ධය",
                "correct": "සිවිල් යුද්ධය",
                "speak": "sivil yudhdhaya"
            },
            {
                "question": "දෙවන ලෝක යුද්ධ සමයේ සෝවියට් සංගමයේ නායකයා කවුද?",
                "a": "ව්ලැඩිමීර් ලෙනින්",
                "b": "ජෝසප් ස්ටාලින්",
                "c": "නිකිටා කෘෂෙව්",
                "d": "ලියොනිඩ් බ්‍රෙෂ්නෙව්",
                "correct": "ජෝසප් ස්ටාලින්",
                "speak": "joseph starlin"
            },
            {
                "question": "ටයිටැනික් නෞකාව ගිලී ගියේ කුමන වසරේද?",
                "a": "1908",
                "b": "1910",
                "c": "1912",
                "d": "1914",
                "correct": "1912",
                "speak": "ekdahas nawasiya dolaha"
            },
            {
                "question": "කොමියුනිස්ට් ප්‍රකාශනය ලිව්වේ කවුද?",
                "a": "කාල් මාක්ස්",
                "b": "ව්ලැඩිමීර් ලෙනින්",
                "c": "ෆ්‍රෙඩ්රික් එංගල්ස්",
                "d": "මාඕ සේතුං",
                "correct": "කාල් මාක්ස්",
                "speak": "kal maks"
            },
            {
                "question": "ඇඩොල්ෆ් හිට්ලර් උපත ලැබුවේ කුමන රටේද?",
                "a": "ජර්මනිය",
                "b": "ඔස්ට්‍රියාව",
                "c": "පෝලන්තය",
                "d": "හංගේරියාව",
                "correct": "ඔස්ට්‍රියාව",
                "speak": "ostriyawa"
            },
            {
                "question": "සොක්‍රටීස් සහ ප්ලේටෝ වැනි දාර්ශනිකයන් සඳහා ප්‍රසිද්ධ වූ පැරණි ශිෂ්ටාචාරය කුමක්ද?",
                "a": "රෝම",
                "b": "ග්‍රීක",
                "c": "ඊජිප්තු",
                "d": "චීන",
                "correct": "ග්‍රීක",
                "speak": "greeka"
            },
            {
                "question": "එක්සත් ජනපදය පළමු මිනිසා සඳ මත ගොඩ බැස්සේ කුමන වසරේද?",
                "a": "1967",
                "b": "1968",
                "c": "1969",
                "d": "1970",
                "correct": "1969",
                "speak": "ekdahas nawasiya hata nwaya"
            },
            {
                "question": "දෙවන ලෝක යුද්ධ සමයේ බ්‍රිතාන්‍ය අගමැති කවුද?",
                "a": "නෙවිල් චේම්බර්ලයින්",
                "b": "වින්ස්ටන් චර්චිල්",
                "c": "ක්ලෙමන්ට් ඇට්ලි",
                "d": "හැරල්ඩ් මැක්මිලන්",
                "correct": "වින්ස්ටන් චර්චිල්",
                "speak": "winston cherchil"
            },
            {
                "question": "සැමියන් හය දෙනෙකු සිටි ප්‍රසිද්ධ රැජින කවුද?",
                "a": "එලිසබෙත් අයි",
                "b": "මේරි අයි",
                "c": "මහා කැතරින්",
                "d": "හෙන්රි VIII",
                "correct": "හෙන්රි VIII",
                "speak": "atawana henry"
            },
            {
                "question": "සෝවියට් සංගමය බිඳ වැටුනේ කුමන වසරේද?",
                "a": "1989",
                "b": "1990",
                "c": "1991",
                "d": "1992",
                "correct": "1991",
                "speak": "ekdahasnayawasiya anu eka"
            },
            {
                "question": "චීනයේ පළමු අධිරාජ්‍යයා කවුද?",
                "a": "Qin Shi Huang",
                "b": "ලියු බං",
                "c": "ජෙන්ගිස් ඛාන්",
                "d": "කුබ්ලායි ඛාන්",
                "correct": "Qin Shi Huang",
                "speak": "Qin Shi Huang"
            },
            {
                "question": "රෝදය සොයාගැනීමේ ගෞරවය හිමිවන්නේ කුමන පැරණි ශිෂ්ටාචාරයටද?",
                "a": "ඊජිප්තුවරුන්",
                "b": "ග්‍රීක",
                "c": "සුමේරියානුවන්",
                "d": "රෝමවරුන්",
                "correct": "සුමේරියානුවන්",
                "speak": "sumeriyaniwan"
            },
            {
                "question": "රුසියාවේ අවසාන සාර් කවුද?",
                "a": "ඇලෙක්සැන්ඩර් III",
                "b": "නිකලස් II",
                "c": "මහා පීටර්",
                "d": "අයිවන් ද ටෙරිබල්",
                "correct": "නිකලස් II",
                "speak": "dewana nikalas"
            },
            {
                "question": "චීන මහා ප්‍රාකාරයේ ප්‍රධාන අරමුණ කුමක්ද?",
                "a": "වෙළඳ",
                "b": "ප්‍රවාහනය",
                "c": "ආරක්ෂක",
                "d": "කෘෂිකර්ම",
                "correct": "ආරක්ෂක",
                "speak": "arakshaka"
            },
            {
                "question": "විමුක්ති ප්‍රකාශය නිකුත් කළේ කුමන එක්සත් ජනපද ජනාධිපතිවරයාද?",
                "a": "ජෝර්ජ් වොෂින්ටන්",
                "b": "තෝමස් ජෙෆර්සන්",
                "c": "ඒබ්රහම් ලින්කන්",
                "d": "තියඩෝර් රූස්වෙල්ට්",
                "correct": "ඒබ්රහම් ලින්කන්",
                "speak": "ebraham linken"
            },
            {
                "question": "2023 වන විට එක්සත් ජනපදයේ ජනාධිපතිවරයා කවුද?",
                "a": "ඩොනල්ඩ් ට්රම්ප්",
                "b": "ජෝ බයිඩන්",
                "c": "බරක් ඔබාමා",
                "d": "ජෝර්ජ් W බුෂ්",
                "correct": "ජෝ බයිඩන්",
                "speak": "jo baidin"
            },
            {
                "question": "මෑතකදී යුරෝපා සංගමයෙන් ඉවත් වූ රට කුමක්ද?",
                "a": "ප්‍රංශය",
                "b": "ජර්මනිය",
                "c": "එක්සත් රාජධානිය",
                "d": "ඉතාලිය",
                "correct": "එක්සත් රාජධානිය",
                "speak": "eksath rajadaniya"
            },
            {
                "question": "කැනඩාවේ අගමැති කවුද?",
                "a": "ස්ටීවන් හාපර්",
                "b": "ජස්ටින් ටෲඩෝ",
                "c": "ඇන්ඩෘ ෂියර්",
                "d": "ජග්මීත් සිං",
                "correct": "ජස්ටින් ටෲඩෝ",
                "speak": "jastin truudo"
            },
            {
                "question": "2022 ශීත ඍතු ඔලිම්පික් උළෙල පැවැත්වූ රට කුමක්ද?",
                "a": "රුසියාව",
                "b": "ජපානය",
                "c": "චීනය",
                "d": "දකුණු කොරියාව",
                "correct": "චීනය",
                "speak": "chinaya"
            },
            {
                "question": "ලෝකයේ විශාලතම ආර්ථිකය ඇති රට කුමක්ද?",
                "a": "චීනය",
                "b": "එක්සත් ජනපදය",
                "c": "ජපානය",
                "d": "ජර්මනිය",
                "correct": "එක්සත් ජනපදය",
                "speak": "eksath janapadaya"
            },
            {
                "question": "මෑතකදී එහි ප්‍රථම කාන්තා ජනාධිපතිවරිය තේරී පත් වූ අප්‍රිකානු රට කුමක්ද?",
                "a": "ලයිබීරියාව",
                "b": "ඉතියෝපියාව",
                "c": "ඝානාව",
                "d": "ටැන්සානියාව",
                "correct": "ටැන්සානියාව",
                "speak": "tansaniyawa"
            },
            {
                "question": "එමානුවෙල් මැක්‍රොන් විසින් ආරම්භ කරන ලද දේශපාලන පක්ෂයේ නම කුමක්ද?",
                "a": "The Republicans",
                "b": "Socialist Party",
                "c": "La République En Marche!",
                "d": "National Rally",
                "correct": "La République En Marche!",
                "speak": "La République En Marche!"
            },
            {
                "question": "මධ්‍යස්ථ ප්‍රතිපත්තිය සඳහා ප්‍රසිද්ධ රට කුමක්ද?",
                "a": "ස්විට්සර්ලන්තය",
                "b": "ස්වීඩනය",
                "c": "නෝර්වේ",
                "d": "ෆින්ලන්තය",
                "correct": "ස්විට්සර්ලන්තය",
                "speak": "swistserlanthaya"
            },
            {
                "question": "නිව් යෝර්ක් නගරයේ මූලස්ථානය පිහිටා ඇති ජාත්‍යන්තර සංවිධානය කුමක්ද?",
                "a": "නේටෝ",
                "b": "එක්සත් ජාතීන්",
                "c": "යුරෝපනු සංගමය",
                "d": "ලෝක බැංකුව",
                "correct": "එක්සත් ජාතීන්",
                "speak": "eksath jathin"
            },
            {
                "question": "2017 නිදහස පිළිබඳ ජනමත විචාරණයක් පැවැත්වූ රට කුමක්ද?",
                "a": "කැටලෝනියාව (ස්පාඤ්ඤය)",
                "b": "ස්කොට්ලන්තය (එක්සත් රාජධානිය)",
                "c": "ක්විබෙක් (කැනඩාව)",
                "d": "ටිබෙට් (චීනය)",
                "correct": "කැටලෝනියාව (ස්පාඤ්ඤය)",
                "speak": "kata loniyawa hewath spangraya"
            },
            {
                "question": "විශාලතම බොරතෙල් නිෂ්පාදකයා වන රට කුමක්ද?",
                "a": "රුසියාව",
                "b": "සවුදි අරාබිය",
                "c": "එක්සත් ජනපදය",
                "d": "ඉරානය",
                "correct": "එක්සත් ජනපදය",
                "speak": "eksath janapadaya"
            },
            {
                "question": "දැඩි අන්තර්ජාල වාරණ ප්‍රතිපත්ති සඳහා ප්‍රසිද්ධ රට කුමක්ද?",
                "a": "උතුරු කොරියාව",
                "b": "චීනය",
                "c": "ඉරානය",
                "d": "සවුදි අරාබිය",
                "correct": "චීනය",
                "speak": "chinaya"
            },
            {
                "question": "ලෝකයේ වැඩිම ජනගහනයක් සිටින රට කුමක්ද?",
                "a": "ඉන්දියාව",
                "b": "එක්සත් ජනපදය",
                "c": "චීනය",
                "d": "ඉන්දුනීසියාව",
                "correct": "ඉන්දියාව",
                "speak": "indiyawa"
            },
            {
                "question": "ජපානයේ භාවිතා කරන මුදල් ඒකකයේ නම කුමක්ද?",
                "a": "Yuan",
                "b": "Won",
                "c": "Yen",
                "d": "Ruble",
                "correct": "Yen",
                "speak": "Yen"
            },
            {
                "question": "ලෝකයේ විශාලතම ප්‍රජාතන්ත්‍රවාදී රට කුමක්ද?",
                "a": "එක්සත් ජනපදය",
                "b": "ඉන්දියාව",
                "c": "බ්‍රසීලය",
                "d": "ඉන්දුනීසියාව",
                "correct": "ඉන්දියාව",
                "speak": "indiyawa"
            },
            {
                "question": "ජාත්‍යන්තර වෙළඳාම නියාමනය කිරීම සඳහා වගකිව යුතු සංවිධානය කුමක්ද?",
                "a": "IMF",
                "b": "ලෝක බැංකුව",
                "c": "WTO",
                "d": "යුනෙස්කෝව",
                "correct": "WTO",
                "speak": "W T O"
            },
            {
                "question": "විශාලතම කෝපි නිෂ්පාදකයා වන රට කුමක්ද?",
                "a": "කොලොම්බියාව",
                "b": "වියට්නාමය",
                "c": "බ්‍රසීලය",
                "d": "ඉතියෝපියාව",
                "correct": "බ්‍රසීලය",
                "speak": "brasiyalaya"
            },
            {
                "question": "2011 සිට සිවිල් යුද්ධයක පවතින මැද පෙරදිග රට කුමක්ද?",
                "a": "ඉරාකය",
                "b": "සිරියාව",
                "c": "ලිබියාව",
                "d": "යේමනය",
                "correct": "සිරියාව",
                "speak": "siriyawa"
            },
            {
                "question": "'Moby-Dick' ලිව්වේ කවුද?",
                "a": "හර්මන් මෙල්විල්",
                "b": "මාර්ක් ට්වේන්",
                "c": "නතානියෙල් හෝතෝර්න්",
                "d": "එඩ්ගා ඇලන් පෝ",
                "correct": "හර්මන් මෙල්විල්",
                "speak": "herman melwin"
            },
            {
                "question": "'1984' කතුවරයා කවුද?",
                "a": "ඇල්ඩස් හක්ස්ලි",
                "b": "ජෝර්ජ් ඕවල්",
                "c": "රේ බ්‍රැඩ්බරි",
                "d": "අයිසැක් අසිමොව්",
                "correct": "ජෝර්ජ් ඕවල්",
                "speak": "jorj owel"
            },
            {
                "question": "‘Call me Ishmael’ යන පේළියෙන් ආරම්භ වන්නේ කුමන නවකතාවද?",
                "a": "මොබි-ඩික්",
                "b": "Scarlet Letter",
                "c": "උසස් බලාපොරොත්තු",
                "d": "යුද්ධය සහ සාමය",
                "correct": "මොබි-ඩික්",
                "speak": "mobi dick"
            },
            {
                "question": "'The Great Gatsby' ලිව්වේ කවුද?",
                "a": "F. Scott Fitzgerald",
                "b": "අර්නස්ට් හෙමිංවේ",
                "c": "ජෝන් ස්ටයින්බෙක්",
                "d": "විලියම් ෆෝක්නර්",
                "correct": "F. Scott Fitzgerald",
                "speak": "F. Scott Fitzgerald"
            },
            {
                "question": "'Pride and Prejudice' කෘතියේ කතුවරයා කවුද?",
                "a": "එමිලි බ්‍රොන්ටේ",
                "b": "ජේන් ඔස්ටින්",
                "c": "මේරි ෂෙලි",
                "d": "චාලට් බ්‍රොන්ටේ",
                "correct": "ජේන් ඔස්ටින්",
                "speak": "jen ostin"
            },
            {
                "question": "Rosencrantz සහ Guildenstern යන චරිත නිරූපණය කරන Shakespeare නාට්‍යය කුමක්ද?",
                "a": "හැම්ලට්",
                "b": "මැක්බත්",
                "c": "ඔතෙලෝ",
                "d": "ලියර් රජු",
                "correct": "හැම්ලට්",
                "speak": "hamlet"
            },
            {
                "question": "'The Catcher in the Rye' ලිව්වේ කවුද?",
                "a": "JD Salinger",
                "b": "හාපර් ලී",
                "c": "JK රෝලින්",
                "d": "ජෝන් ස්ටයින්බෙක්",
                "correct": "JD Salinger",
                "speak": "JD Salinger"
            },
            {
                "question": "Atticus Finch චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "JD Salinger",
                "b": "හාපර් ලී",
                "c": "JK රෝලින්",
                "d": "ජෝන් ස්ටයින්බෙක්",
                "correct": "JD Salinger",
                "speak": "JD Salinger"
            },
            {
                "question": "The Hobbit කෘතියේ කතුවරයා කවුද?",
                "a": "සීඑස් ලුවිස්",
                "b": "JRR ටොල්කියන්",
                "c": "ජෝර්ජ් ආර්ආර් මාටින්",
                "d": "ටෙරී ප්‍රචෙට්",
                "correct": "JRR ටොල්කියන්",
                "speak": "JRR tolkiyan"
            },
            {
                "question": "'The Raven' ලියූ කවියා කවුද?",
                "a": "රොබට් ෆ්රොස්ට්",
                "b": "වෝල්ට් විට්මන්",
                "c": "එඩ්ගා ඇලන් පෝ",
                "d": "එමිලි ඩිකින්සන්",
                "correct": "එඩ්ගා ඇලන් පෝ",
                "speak": "edga alen poo"
            },
            {
                "question": "'Brave New World' ලිව්වේ කවුද?",
                "a": "ජෝර්ජ් ඕවල්",
                "b": "ඇල්ඩස් හක්ස්ලි",
                "c": "රේ බ්‍රැඩ්බරි",
                "d": "කර්ට් වොනෙගුට්",
                "correct": "ඇල්ඩස් හක්ස්ලි",
                "speak": "aldas haksli"
            },
            {
                "question": "'හැරී පොටර්' කතුවරයා කවුද?",
                "a": "JK රෝලින්",
                "b": "සුසෑන් කොලින්ස්",
                "c": "ස්ටීවන් කිං",
                "d": "රික් රියෝඩන්",
                "correct": "JK රෝලින්",
                "speak": "JK rolin"
            },
            {
                "question": "Elizabeth Bennet චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "දැනීම් සහ දැනීම",
                "b": "ප්‍රයිඩ් ඇන්ඩ් ප්‍රයිජුඩ්",
                "c": "එමා",
                "d": "ඒත්තු ගැන්වීම",
                "correct": "ප්‍රයිඩ් ඇන්ඩ් ප්‍රයිජුඩ්",
                "speak": "prayid and prayijud"
            },
            {
                "question": "'The Odyssey' ලිව්වේ කවුද?",
                "a": "හෝමර්",
                "b": "වර්ජිල්",
                "c": "සොෆොක්ලීස්",
                "d": "යුරිපිඩීස්",
                "correct": "හෝමර්",
                "speak": "homer"
            },
            {
                "question": "‘එය හොඳම කාලයයි, නරකම කාලයයි’ යන පේළියෙන් ආරම්භ වන්නේ කුමන නවකතාවද?",
                "a": "Moby-Dick",
                "b": "A Tale of Two Cities",
                "c": "Great Expectations",
                "d": "The Scarlet Letter",
                "correct": "A Tale of Two Cities",
                "speak": "A Tale of Two Cities"
            },
            {
                "question": "'The Chronicles of Narnia' ලිව්වේ කවුද?",
                "a": "JK රෝලින්",
                "b": "JRR ටොල්කියන්",
                "c": "CS ලුවිස්",
                "d": "පිලිප් පුල්මන්",
                "correct": "CS ලුවිස්",
                "speak": "C S Luvis"
            },
            {
                "question": "Jay Gatsby චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "The Great Gatsby",
                "b": "To Kill a Mockingbird",
                "c": "The Catcher in the Rye",
                "d": "The Grapes of Wrath",
                "correct": "The Great Gatsby",
                "speak": "The Great Gatsby"
            },
            {
                "question": "'ෆ්‍රැන්කන්ස්ටයින්' ලිව්වේ කවුද?",
                "a": "මේරි ෂෙලි",
                "b": "බ්‍රැම් ස්ටෝකර්",
                "c": "එච්ජී වෙල්ස්",
                "d": "ජූල්ස් වර්න්",
                "correct": "මේරි ෂෙලි",
                "speak": "meery shely"
            },
            {
                "question": "The Lord of the Rings කෘතියේ කතුවරයා කවුද?",
                "a": "ජෝර්ජ් RR මාටින්",
                "b": "CS ලුවිස්",
                "c": "JK රෝලින්",
                "d": "JRR ටොල්කියන්",
                "correct": "JRR ටොල්කියන්",
                "speak": "J R R tolkiyan"
            },
            {
                "question": "ෂර්ලොක් හෝම්ස් චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "Dracula",
                "b": "The Hound of the Baskervilles",
                "c": "The Great Gatsby",
                "d": "To Kill a Mockingbird",
                "correct": "The Hound of the Baskervilles",
                "speak": "The Hound of the Baskervilles"
            },
            {
                "question": "'ඩ්‍රැකියුලා' ලිව්වේ කවුද?",
                "a": "මේරි ෂෙලි",
                "b": "බ්‍රැම් ස්ටෝකර්",
                "c": "එච්ජී වෙල්ස්",
                "d": "ජූල්ස් වර්න්",
                "correct": "බ්‍රැම් ස්ටෝකර්",
                "speak": "bram stoker"
            },
            {
                "question": "The Catch-22 හි කතුවරයා කවුද?",
                "a": "ජෝසප් හෙලර්",
                "b": "කර්ට් වොනෙගුට්",
                "c": "ජෝර්ජ් ඕවල්",
                "d": "ඇල්ඩස් හක්ස්ලි",
                "correct": "ජෝසප් හෙලර්",
                "speak": "joseph heler"
            },
            {
                "question": "හකල්බෙරි ෆින් චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "The Adventures of Huckleberry Finn",
                "b": "The Catcher in the Rye",
                "c": "To Kill a Mockingbird",
                "d": "The Great Gatsby",
                "correct": "The Adventures of Huckleberry Finn",
                "speak": "The Adventures of Huckleberry Finn"
            },
            {
                "question": "'The Count of Monte Cristo' ලිව්වේ කවුද?",
                "a": "ජූල්ස් වර්න්",
                "b": "ඇලෙක්සැන්ඩර් ඩූමාස්",
                "c": "වික්ටර් හියුගෝ",
                "d": "ගුස්ටාව් ෆ්ලෝබර්ට්",
                "correct": "ඇලෙක්සැන්ඩර් ඩූමාස්",
                "speak": "alexander dumas"
            },
            {
                "question": "'යුද්ධය සහ සාමය' කතුවරයා කවුද?",
                "a": "ෆෙඩෝර් දොස්තයෙව්ස්කි",
                "b": "ලියෝ ටෝල්ස්ටෝයි",
                "c": "ඇන්ටන් චෙකොව්",
                "d": "නිකොලායි ගොගොල්",
                "correct": "ලියෝ ටෝල්ස්ටෝයි",
                "speak": "liyo tolstoyi"
            },
            {
                "question": "Frodo Baggins චරිතය නිරූපණය කරන නවකතාව කුමක්ද?",
                "a": "හොබිට්",
                "b": "Silmarillion",
                "c": "ලෝඩ් ඔෆ් ද රින්ග්ස්",
                "d": "The Chronicles of Narnia",
                "correct": "ලෝඩ් ඔෆ් ද රින්ග්ස්",
                "speak": "lood of the rings"
            },
            {
                "question": "'සියවසරක හුදකලාව' ලිව්වේ කවුද?",
                "a": "Gabriel Garcia Marquez",
                "b": "ජෝර්ජ් ලුයිස් බෝර්ජස්",
                "c": "මාරියෝ වර්ගාස් ලෝසා",
                "d": "ඉසබෙල් ඇලෙන්ඩේ",
                "correct": "Gabriel Garcia Marquez",
                "speak": "Gabriel Garcia Marquez"
            },
            {
                "question": "'දොන් ක්වික්සෝට්' හි කතුවරයා කවුද?",
                "a": "Miguel de Cervantes",
                "b": "ජෝර්ජ් ලුයිස් බෝර්ජස්",
                "c": "Gabriel Garcia Marquez",
                "d": "පැබ්ලෝ නෙරූඩා",
                "correct": "Miguel de Cervantes",
                "speak": "Miguel de Cervantes"
            },
            {
                "question": "'අප්‍රේල් මාසයේ දීප්තිමත් සීතල දවසක්, ඔරලෝසු දහතුනක් වැදුණා' යන පේළියෙන් ආරම්භ වන්නේ කුමන නවකතාවද?",
                "a": "Brave New World",
                "b": "1984",
                "c": "Fahrenheit 451",
                "d": "The Handmaid's Tale",
                "correct": "1984",
                "speak": "ekdahas nawasiya asu hathara"
            },
            {
                "question": "ජලය සඳහා රසායනික සංකේතය කුමක්ද?",
                "a": "H2",
                "b": "H2O",
                "c": "HO2",
                "d": "H2O2",
                "correct": "H2O",
                "speak": "H 2 O"
            },
            {
                "question": "රතු ග්‍රහලෝකය ලෙස හඳුන්වන ග්‍රහලෝකය කුමක්ද?",
                "a": "සිකුරු",
                "b": "අඟහරු",
                "c": "බ්‍රහස්පති",
                "d": "සෙනසුරු",
                "correct": "අඟහරු",
                "speak": "agaharu"
            },
            {
                "question": "සාමාන්‍ය සාපේක්ෂතාවාදයේ න්‍යාය වර්ධනය කළේ කවුද?",
                "a": "අයිසැක් නිව්ටන්",
                "b": "ඇල්බට් අයින්ස්ටයින්",
                "c": "නීල්ස් බෝර්",
                "d": "ගැලීලියෝ ගැලීලි",
                "correct": "ඇල්බට් අයින්ස්ටයින්",
                "speak": "albert aistayin"
            },
            {
                "question": "ආලෝකයේ වේගය කුමක්ද?",
                "a": "300,000 km/s",
                "b": "150,000 km/s",
                "c": "200,000 km/s",
                "d": "250,000 km/s",
                "correct": "300,000 km/s",
                "speak": "payata kilometer laksha thunai"
            },
            {
                "question": "නූතන භෞතික විද්‍යාවේ පියා ලෙස හඳුන්වන්නේ කවුද?",
                "a": "අයිසැක් නිව්ටන්",
                "b": "ගැලීලියෝ ගැලීලි",
                "c": "ඇල්බට් අයින්ස්ටයින්",
                "d": "නීල්ස් බෝර්",
                "correct": "ගැලීලියෝ ගැලීලි",
                "speak": "galiliyo galili"
            },
            {
                "question": "පෙනිසිලින් සොයාගත්තේ කවුද?",
                "a": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
                "b": "මාරි කියුරි",
                "c": "ලුවී පාස්චර්",
                "d": "Gregor Mendel",
                "correct": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
                "speak": "alexander plemin"
            },
            {
                "question": "ජීවයේ කුඩාම ඒකකය කුමක්ද?",
                "a": "පරමාණුව",
                "b": "අණුව",
                "c": "සෛලය",
                "d": "ජීවියා",
                "correct": "සෛලය",
                "speak": "sailaya"
            },
            {
                "question": "මේස ලුණු සඳහා රසායනික සූත්රය කුමක්ද?",
                "a": "NaCl",
                "b": "KCl",
                "c": "Na2SO4",
                "d": "K2SO4",
                "correct": "NaCl",
                "speak": "N A C L"
            },
            {
                "question": "චලිත නීති යෝජනා කළේ කවුද?",
                "a": "ඇල්බට් අයින්ස්ටයින්",
                "b": "ගැලීලියෝ ගැලීලි",
                "c": "අයිසැක් නිව්ටන්",
                "d": "නීල්ස් බෝර්",
                "correct": "අයිසැක් නිව්ටන්",
                "speak": "aisak newten"
            },
            {
                "question": "පෘථිවියේ ඇති ඝනකන්ම ස්වභාවික ද්‍රව්‍යය කුමක්ද?",
                "a": "රන්",
                "b": "යකඩ",
                "c": "දියමන්ති",
                "d": "ක්වාර්ට්ස්",
                "correct": "දියමන්ති",
                "speak": "diayamanthi"
            },
            {
                "question": "සූර්යයාගේ සංයුතියේ මූලික වායුව කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "හයිඩ්රජන්",
                "c": "හීලියම්",
                "d": "නයිට්රජන්",
                "correct": "හයිඩ්රජන්",
                "speak": "haigragen"
            },
            {
                "question": "ආවර්තිතා වගුවේ 'O' නියෝජනය කරන මූලද්‍රව්‍යය කුමක්ද?",
                "a": "රන්",
                "b": "ඔක්සිජන්",
                "c": "ඔස්මියම්",
                "d": "ඔගනෙසන්",
                "correct": "ඔක්සිජන්",
                "speak": "oxigen"
            },
            {
                "question": "පිරිසිදු ජලයේ pH අගය කුමක්ද?",
                "a": "5",
                "b": "6",
                "c": "7",
                "d": "8",
                "correct": "7",
                "speak": "hathai"
            },
            {
                "question": "බැටරියක ගබඩා වන්නේ කුමන ආකාරයේ ශක්තියක්ද?",
                "a": "චාලක",
                "b": "තාප",
                "c": "රසායනික",
                "d": "යාන්ත්‍රික",
                "correct": "රසායනික",
                "speak": "rasayanika"
            },
            {
                "question": "උරුමය පිළිබඳ නීති සඳහා ප්‍රසිද්ධ වන්නේ කවුද?",
                "a": "චාල්ස් ඩාවින්",
                "b": "Gregor Mendel",
                "c": "ලුවී පාස්චර්",
                "d": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
                "correct": "Gregor Mendel",
                "speak": "Gregor Mendel"
            },
            {
                "question": "සූර්යයාට සමීපතම ග්‍රහලෝකය කුමක්ද?",
                "a": "සිකුරු",
                "b": "අඟහරු",
                "c": "බුධ",
                "d": "පොළොවේ",
                "correct": "බුධ",
                "speak": "bugha"
            },
            {
                "question": "පරමාණුවක කේන්ද්‍රය හඳුන්වන්නේ කුමක්ද?",
                "a": "ඉලෙක්ට්‍රෝනය",
                "b": "ප්රෝටෝනය",
                "c": "න්‍යෂ්ටිය",
                "d": "නියුට්‍රෝනය",
                "correct": "න්‍යෂ්ටිය",
                "speak": "nyastiya"
            },
            {
                "question": "ශාක පිළිබඳ අධ්‍යයනය හඳුන්වන්නේ කුමක්ද?",
                "a": "සත්ව විද්‍යාව",
                "b": "භූ විද්‍යාව",
                "c": "උද්භිද විද්‍යාව",
                "d": "පරිසර විද්‍යාව",
                "correct": "උද්භිද විද්‍යාව",
                "speak": "udbhitha widyawa"
            },
            {
                "question": "මිනිස් සිරුරේ විශාලතම ඉන්ද්‍රිය කුමක්ද?",
                "a": "හදවත",
                "b": "අක්මාව",
                "c": "සම",
                "d": "පෙනහළු",
                "correct": "සම",
                "speak": "sama"
            },
            {
                "question": "රත්රන් සඳහා රසායනික සංකේතය කුමක්ද?",
                "a": "Ag",
                "b": "Au",
                "c": "Pb",
                "d": "Fe",
                "correct": "Au",
                "speak": "A U"
            },
            {
                "question": "ජානමය ද්‍රව්‍ය අඩංගු සෛලයේ කුමන කොටසේද?",
                "a": "සයිටොප්ලාස්මය",
                "b": "මයිටොකොන්ඩ්‍රියා",
                "c": "න්‍යෂ්ටිය",
                "d": "සෛල පටලය",
                "correct": "න්‍යෂ්ටිය",
                "speak": "nyashtiya"
            },
            {
                "question": "අපව පෘථිවිය මත රඳවා තබන බලවේගය කුමක්ද?",
                "a": "චුම්භකත්වය",
                "b": "විද්යුත් චුම්භකත්වය",
                "c": "ගුරුත්වාකර්ෂණය",
                "d": "ඝර්ෂණය",
                "correct": "ගුරුත්වාකර්ෂණය",
                "speak": "guruthwakarshanaya"
            },
            {
                "question": "විශ්වයේ බහුලවම ඇති මූලද්‍රව්‍යය කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "හයිඩ්රජන්",
                "c": "හීලියම්",
                "d": "කාබන්",
                "correct": "හයිඩ්රජන්",
                "speak": "haidragen"
            },
            {
                "question": "පරිණාමයේ පියා ලෙස හඳුන්වන්නේ කවුද?",
                "a": "අයිසැක් නිව්ටන්",
                "b": "චාල්ස් ඩාවින්",
                "c": "Gregor Mendel",
                "d": "ඇල්බට් අයින්ස්ටයින්",
                "correct": "චාල්ස් ඩාවින්",
                "speak": "chales dawin"
            },
            {
                "question": "කාබන් ඩයොක්සයිඩ් සඳහා රසායනික සුත්‍රය කුමක්ද?",
                "a": "CO",
                "b": "CO2",
                "c": "C2O",
                "d": "O2",
                "correct": "CO2",
                "speak": "C O deka"
            },
            {
                "question": "තරු සහ ග්‍රහලෝක පිළිබඳ අධ්‍යයනය හඳුන්වන්නේ කුමක්ද?",
                "a": "භූ විද්‍යාව",
                "b": "ජීව විද්‍යාව",
                "c": "තාරකා විද්‍යාව",
                "d": "රසායන විද්‍යාව",
                "correct": "තාරකා විද්‍යාව",
                "speak": "tharaka widyawa"
            },
            {
                "question": "ආවර්තිතා වගුව නිර්මාණය කළේ කවුද?",
                "a": "මාරි කියුරි",
                "b": "දිමිත්‍රි මෙන්ඩලීව්",
                "c": "නීල්ස් බෝර්",
                "d": "ඇල්බට් අයින්ස්ටයින්",
                "correct": "දිමිත්‍රි මෙන්ඩලීව්",
                "speak": "dimithri mendeliw"
            },
            {
                "question": "අපගේ සෞරග්‍රහ මණ්ඩලයේ විශාලතම ග්‍රහලෝකය කුමක්ද?",
                "a": "පොළොවේ",
                "b": "සෙනසුරු",
                "c": "බ්‍රහස්පති",
                "d": "නෙප්චූන්",
                "correct": "බ්‍රහස්පති",
                "speak": "brahaspathi"
            },
            {
                "question": "පෘථිවි වායුගෝලයේ බහුලවම ඇති වායුව කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "කාබන් ඩයොක්සයිඩ්",
                "c": "නයිට්‍රජන්",
                "d": "හයිඩ්රජන්",
                "correct": "නයිට්‍රජන්",
                "speak": "naitrogen"
            },
            {
                "question": "අප ආශ්වාස කරන වාතයේ ඇති ප්‍රධාන වායුව කුමක්ද?",
                "a": "ඔක්සිජන්",
                "b": "කාබන් ඩයොක්සයිඩ්",
                "c": "හයිඩ්රජන්",
                "d": "නයිට්‍රජන්",
                "correct": "නයිට්‍රජන්",
                "speak": "naitrogen"
            },
            {
                "question": "ජාන විද්‍යාවේ පියා ලෙස හඳුන්වන්නේ කවුද?",
                "a": "චාල්ස් ඩාවින්",
                "b": "Gregor Mendel",
                "c": "ලුවී පාස්චර්",
                "d": "ඇලෙක්සැන්ඩර් ෆ්ලෙමින්",
                "correct": "Gregor Mendel",
                "speak": "Gregor Mendel"
            },
            {
                "question": "ජීවිතයේ මූලික ඒකකය කුමක්ද?",
                "a": "පරමාණුව",
                "b": "අණුව",
                "c": "සෛලය",
                "d": "පටක",
                "correct": "සෛලය",
                "speak": "sailaya"
            },
            {
                "question": "ප්‍රංශයේ අගනුවර කුමක්ද?",
                "a": "බර්ලින්",
                "b": "මැඩ්රිඩ්",
                "c": "රෝමය",
                "d": "පැරිස්",
                "correct": "පැරිස්",
                "speak": "parisiya"
            },
            {
                "question": "භූමි ප්‍රමාණය අනුව විශාලතම මහාද්වීපය කුමක්ද?",
                "a": "අප්‍රිකාව",
                "b": "ආසියාව",
                "c": "යුරෝපය",
                "d": "ඇන්ටාක්ටිකාව",
                "correct": "ආසියාව",
                "speak": "asiyawa"
            },
            {
                "question": "ලෝකයේ දිගම ගංගාව කුමක්ද?",
                "a": "ඇමසන් ගඟ",
                "b": "නයිල් ගඟ",
                "c": "යැංසි ගඟ",
                "d": "මිසිසිපි ගඟ",
                "correct": "නයිල් ගඟ",
                "speak": "nail gaga"
            },
            {
                "question": "එවරස්ට් කන්ද පිහිටා ඇත්තේ කුමන කඳු පන්තියේද?",
                "a": "ඇන්ඩීස්",
                "b": "රොකීස්",
                "c": "හිමාලය",
                "d": "ඇල්ප්ස්",
                "correct": "හිමාලය",
                "speak": "himalaya"
            },
            {
                "question": "ඕස්ට්‍රේලියාවේ අගනුවර කුමක්ද?",
                "a": "සිඩ්නි",
                "b": "මෙල්බර්න්",
                "c": "බ්රිස්බේන්",
                "d": "කැන්බරා",
                "correct": "කැන්බරා",
                "speak": "kanbara"
            },
            {
                "question": "භූමි ප්‍රමාණය අනුව විශාලතම රට කුමක්ද?",
                "a": "කැනඩාව",
                "b": "එක්සත් ජනපදය",
                "c": "රුසියාව",
                "d": "චීනය",
                "correct": "රුසියාව",
                "speak": "rusiyawa"
            },
            {
                "question": "ගැඹුරුම සාගරය කුමක්ද?",
                "a": "අත්ලාන්තික් සාගරය",
                "b": "ඉන්දියන් සාගරය",
                "c": "ආක්ටික් සාගරය",
                "d": "ශාන්තිකර සාගරය",
                "correct": "ශාන්තිකර සාගරය",
                "speak": "shanthikara sagaraya"
            },
            {
                "question": "ලෝකයේ දිගම කඳු වැටිය කුමක්ද?",
                "a": "රොකීස්",
                "b": "ඇන්ඩීස්",
                "c": "හිමාලය",
                "d": "ඇල්ප්ස්",
                "correct": "ඇන්ඩීස්",
                "speak": "andees"
            },
            {
                "question": "වැඩිම ජනගහනයක් සිටින රට කුමක්ද?",
                "a": "ඉන්දියාව",
                "b": "එක්සත් ජනපදය",
                "c": "චීනය",
                "d": "ඉන්දුනීසියාව",
                "correct": "චීනය",
                "speak": "chinaya"
            },
            {
                "question": "කැනඩාවේ අගනුවර කුමක්ද?",
                "a": "ටොරොන්ටෝ",
                "b": "වැන්කුවර්",
                "c": "ඔටාවා",
                "d": "මොන්ට්‍රියල්",
                "correct": "ඔටාවා",
                "speak": "otawa"
            },
            {
                "question": "ලෝකයේ විශාලතම දූපත කුමක්ද?",
                "a": "බෝර්නියෝ",
                "b": "නිව් ගිනියාව",
                "c": "ග්‍රීන්ලන්තය",
                "d": "මැඩගස්කරය",
                "correct": "ග්‍රීන්ලන්තය",
                "speak": "greenlanthaya"
            },
            {
                "question": "ජපානයේ අගනුවර කුමක්ද?",
                "a": "සෝල්",
                "b": "බීජිං",
                "c": "ටෝකියෝ",
                "d": "කියෝතෝ",
                "correct": "ටෝකියෝ",
                "speak": "tokiyo"
            },
            {
                "question": "භූමි ප්‍රමාණය අනුව විශාලතම එක්සත් ජනපද ප්‍රාන්තය කුමක්ද?",
                "a": "කැලිෆෝනියාව",
                "b": "ටෙක්සාස්",
                "c": "ඇලස්කාව",
                "d": "මොන්ටානා",
                "correct": "ඇලස්කාව",
                "speak": "aleskawa"
            },
            {
                "question": "ලෝකයේ කුඩාම සාගරය කුමක්ද?",
                "a": "අත්ලාන්තික් සාගරය",
                "b": "ඉන්දියන් සාගරය",
                "c": "දකුණු සාගරය",
                "d": "ආක්ටික් සාගරය",
                "correct": "ආක්ටික් සාගරය",
                "speak": "aktik sagaraya"
            },
            {
                "question": "බ්‍රසීලයේ අගනුවර කුමක්ද?",
                "a": "රියෝ ද ජැනයිරෝ",
                "b": "සාඕ පවුලෝ",
                "c": "බ්‍රසිලියා",
                "d": "සැල්වදෝරය",
                "correct": "බ්‍රසිලියා",
                "speak": "brasiiliya"
            },
            {
                "question": "පැරිස් හරහා ගලා යන ගංගාව කුමක්ද?",
                "a": "තේම්ස්",
                "b": "සේයින්",
                "c": "ඩැනියුබ්",
                "d": "රයින්",
                "correct": "සේයින්",
                "speak": "sein"
            },
            {
                "question": "නැගී එන සූර්යයාගේ දේශය ලෙස හඳුන්වන රට කුමක්ද?",
                "a": "චීනය",
                "b": "ජපානය",
                "c": "දකුණු කොරියාව",
                "d": "තායිලන්තය",
                "correct": "ජපානය",
                "speak": "japanaya"
            },
            {
                "question": "සන්ෂයින් ස්ටේට් ලෙස හඳුන්වන එක්සත් ජනපද ප්‍රාන්තය කුමක්ද?",
                "a": "කැලිෆෝනියාව",
                "b": "හවායි",
                "c": "ෆ්ලොරිඩාව",
                "d": "ඇරිසෝනා",
                "correct": "ෆ්ලොරිඩාව",
                "speak": "floridawa"
            },
            {
                "question": "ඉතාලියේ අගනුවර කුමක්ද?",
                "a": "වැනීසිය",
                "b": "මිලාන්",
                "c": "ෆ්ලෝරන්ස්",
                "d": "රෝමය",
                "correct": "රෝමය",
                "speak": "romaya"
            },
            {
                "question": "වැඩිපුරම රටවල් ඇති මහාද්වීපය කුමක්ද?",
                "a": "ආසියාව",
                "b": "අප්‍රිකාව",
                "c": "යුරෝපය",
                "d": "දකුණු ඇමරිකාව",
                "correct": "අප්‍රිකාව",
                "speak": "aprikawa"
            },
            {
                "question": "එක්සත් ජනපදයේ දිගම ගංගාව කුමක්ද?",
                "a": "මිසිසිපි ගඟ",
                "b": "මිසූරි ගඟ",
                "c": "කොලරාඩෝ ගඟ",
                "d": "යුකොන් ගඟ",
                "correct": "මිසූරි ගඟ",
                "speak": "misuri gaga"
            },
            {
                "question": "ඉන්දියාවේ අගනුවර කුමක්ද?",
                "a": "මුම්බායි",
                "b": "කොල්කටා",
                "c": "නව දිල්ලි",
                "d": "බැංගලෝර්",
                "correct": "නව දිල්ලි",
                "speak": "nawa dilli"
            },
            {
                "question": "දෙපාර්තමේන්තු වලට බෙදා ඇති යුරෝපීය රට කුමක්ද?",
                "a": "ජර්මනිය",
                "b": "ඉතාලිය",
                "c": "ප්‍රංශය",
                "d": "ස්පාඤ්ඤය",
                "correct": "ප්‍රංශය",
                "speak": "pranshaya"
            },
            {
                "question": "ඊජිප්තුවේ අගනුවර කුමක්ද?",
                "a": "ඇලෙක්සැන්ඩ්රියාව",
                "b": "කයිරෝ",
                "c": "ගීසා",
                "d": "ලක්සර්",
                "correct": "කයිරෝ",
                "speak": "kairo"
            },
            {
                "question": "ලෑන්ඩ් ඩවුන් අන්ඩර් ලෙස හඳුන්වන රට කුමක්ද?",
                "a": "දකුණු අප්‍රිකාව",
                "b": "නවසීලන්තය",
                "c": "ඕස්ට්‍රේලියාව  ",
                "d": "ෆීජි",
                "correct": "ඕස්ට්‍රේලියාව  ",
                "speak": "ostraliyawa  "
            },
            {
                "question": "රුසියාවේ අගනුවර කුමක්ද?",
                "a": "ශාන්ත පීටර්ස්බර්ග්",
                "b": "මින්ස්ක්",
                "c": "මොස්කව්",
                "d": "කියෙව්",
                "correct": "මොස්කව්",
                "speak": "moscow"
            },
            {
                "question": "අප්‍රිකාවේ උසම කන්ද කුමක්ද?",
                "a": "කෙන්යාවේ කන්ද",
                "b": "කිලිමන්ජාරෝ කන්ද",
                "c": "එල්ගොන් කන්ද",
                "d": "මේරු කන්ද",
                "correct": "කිලිමන්ජාරෝ කන්ද",
                "speak": "kilimanjaro kanda"
            },
            {
                "question": "වැඩිම වේලා කලාප ඇති රට කුමක්ද?",
                "a": "එක්සත් ජනපදය",
                "b": "රුසියාව",
                "c": "චීනය",
                "d": "කැනඩාව",
                "correct": "රුසියාව",
                "speak": "rusiyawa"
            },
            {
                "question": "ජනගහනය අනුව කුඩාම රට කුමක්ද?",
                "a": "මොනාකෝ",
                "b": "නාඌරූ",
                "c": "සැන් මරිනෝ",
                "d": "වතිකානුව",
                "correct": "වතිකානුව",
                "speak": "wathikanuwa"
            },
            {
                "question": "දකුණු කොරියාවේ අගනුවර කුමක්ද?",
                "a": "ටෝකියෝ",
                "b": "සෝල්",
                "c": "බීජිං",
                "d": "පියොංයැං",
                "correct": "සෝල්",
                "speak": "sool"
            },
            {
                "question": "දකුණු ඇමරිකාවේ විශාලතම රට කුමක්ද?",
                "a": "ආර්ජන්ටිනාව",
                "b": "බ්‍රසීලය",
                "c": "පේරු",
                "d": "කොලොම්බියාව",
                "correct": "බ්‍රසීලය",
                "speak": "brasilaya"
            },
            {
                "question": "ලුණු වැඩිම මුහුද කුමක්ද?",
                "a": "කළු මුහුද",
                "b": "බෝල්ටික් මුහුද",
                "c": "රතු මුහුද",
                "d": "මල මුහුද",
                "correct": "මල මුහුද",
                "speak": "mala muhuda"
            },
            {
                "question": "ශ්‍රී ලංකාවේ අගනුවර කුමක්ද?",
                "a": "මහනුවර",
                "b": "ගාල්ල",
                "c": "කොළඹ",
                "d": "යාපනය",
                "correct": "කොළඹ",
                "speak": "kolaba"
            },
            {
                "question": "ශ්‍රී ලංකාවේ නිල භාෂාව කුමක්ද?",
                "a": "හින්දි",
                "b": "ඉංග්රීසි",
                "c": "සිංහල",
                "d": "දෙමළ",
                "correct": "සිංහල",
                "speak": "sinhala"
            },
            {
                "question": "ශ්‍රී ලාංකික කාන්තාවන්ගේ සම්ප්‍රදායික ඇඳුම හඳුන්වන්නේ කුමක්ද?",
                "a": "සාරි",
                "b": "කිමෝනෝ",
                "c": "චියොන්සම්",
                "d": "හැන්බොක්",
                "correct": "සාරි",
                "speak": "sari"
            },
            {
                "question": "ශ්‍රී ලංකාවේ ආලෝකයේ උත්සවය ලෙස හඳුන්වනු ලබන්නේ කුමන උත්සවයද?",
                "a": "වෙසක්",
                "b": "දීවාලි",
                "c": "නත්තල්",
                "d": "රාමසාන්",
                "correct": "වෙසක්",
                "speak": "wesak"
            },
            {
                "question": "ශ්‍රී ලංකාවේ ජාතික ක්‍රීඩාව කුමක්ද?",
                "a": "ක්රිකට්",
                "b": "රග්බි",
                "c": "වොලිබෝල්",
                "d": "පාපන්දු",
                "correct": "වොලිබෝල්",
                "speak": "wolyball"
            },
            {
                "question": "ශ්‍රී ලංකාවෙන් එන ප්‍රසිද්ධ තේ මොනවාද?",
                "a": "ඩාර්ජිලිං",
                "b": "ඇසෑම්",
                "c": "Ceylon",
                "d": "අර්ල් ග්‍රේ",
                "correct": "Ceylon",
                "speak": "Ceylon"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පැරණි අගනුවර කුමක්ද?",
                "a": "මහනුවර",
                "b": "අනුරාධපුර",
                "c": "කොළඹ",
                "d": "ගාල්ල",
                "correct": "අනුරාධපුර",
                "speak": "anuradhapuraya"
            },
            {
                "question": "ශ්‍රී ලංකා ධජයේ දැක්වෙන සත්වයා කුමක්ද?",
                "a": "අලියා",
                "b": "සිංහයා",
                "c": "කොටියා",
                "d": "මොනරා",
                "correct": "සිංහයා",
                "speak": "sinhaya"
            },
            {
                "question": "සාමාන්‍යයෙන් කෙසෙල් කොළයක පිළිගන්වන සාම්ප්‍රදායික ශ්‍රී ලාංකික ආහාර වේලක් කුමක්ද?",
                "a": "තාලි",
                "b": "දෝසා",
                "c": "ලම්ප්රයිස්",
                "d": "සුෂි",
                "correct": "ලම්ප්රයිස්",
                "speak": "lumprice"
            },
            {
                "question": "ශ්‍රී ලංකාවේ වැඩිම අනුගාමිකයන් සිටින ආගම කුමක්ද?",
                "a": "හින්දු ආගම",
                "b": "ඉස්ලාම්",
                "c": "බුද්ධාගම",
                "d": "ක්රිස්තියානි ධර්මය",
                "correct": "බුද්ධාගම",
                "speak": "buddagama"
            },
            {
                "question": "සාම්ප්‍රදායික ශ්‍රී ලාංකික බෙරයේ නම කුමක්ද?",
                "a": "තබ්ලා",
                "b": "දෝල්",
                "c": "තම්මට්ටම",
                "d": "ඩිජෙම්බේ",
                "correct": "තම්මට්ටම",
                "speak": "thammattama"
            },
            {
                "question": "පර්වතයක් මත ඉදිකර ඇති සුප්‍රසිද්ධ ශ්‍රී ලංකා බලකොටුවේ නම කුමක්ද?",
                "a": "සීගිරිය",
                "b": "ගාලු කොටුව",
                "c": "පොළොන්නරුව",
                "d": "දඹුල්ල",
                "correct": "සීගිරිය",
                "speak": "sigiriya"
            },
            {
                "question": "උඩරට සාම්ප්‍රදායික නැටුම් ක්‍රමය කුමක්ද?",
                "a": "භරතනාට්‍යය",
                "b": "කතක්",
                "c": "උඩරට නර්තනය",
                "d": "ඔඩිසි",
                "correct": "උඩරට නර්තනය",
                "speak": "udarata narthanaya"
            },
            {
                "question": "පූජනීය දළදා මාලිගාව සඳහා ප්‍රසිද්ධ ශ්‍රී ලංකා නගරය කුමක්ද?",
                "a": "කොළඹ",
                "b": "ගාල්ල",
                "c": "මහනුවර",
                "d": "යාපනය",
                "correct": "මහනුවර",
                "speak": "mahanuwara"
            },
            {
                "question": "ශ්‍රී ලංකාවේ මුදල් ඒකකය යනු කුමක්ද?",
                "a": "රුපියල",
                "b": "ඩොලර්",
                "c": "පවුම්",
                "d": "යුරෝ",
                "correct": "රුපියල",
                "speak": "rupiyala"
            },
            {
                "question": "සිංහල සහ දෙමළ අලුත් අවුරුද්ද සමරන ශ්‍රී ලාංකික උත්සවය කුමක්ද?",
                "a": "වෙසක්",
                "b": "පෝය",
                "c": "අවුරුදු",
                "d": "දීපවාලි",
                "correct": "අවුරුදු",
                "speak": "awrudu"
            },
            {
                "question": "සටන් සහ නැටුම් යන දෙකම ඇතුළත් ශ්‍රී ලාංකේය සටන් කලාවේ නම කුමක්ද?",
                "a": "කරාටේ",
                "b": "කලරිපයට්ටු",
                "c": "අංගම්පොර",
                "d": "ටයිකොන්ඩෝ",
                "correct": "අංගම්පොර",
                "speak": "angampora"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පොල් සම්බෝලයේ ප්‍රධාන අමුද්‍රව්‍යය කුමක්ද?",
                "a": "තක්කාලි",
                "b": "පොල්",
                "c": "ලූනු",
                "d": "සුදුළුනු",
                "correct": "පොල්",
                "speak": "pol"
            },
            {
                "question": "ශ්‍රී ලංකාවේ 'සංස්කෘතික අගනුවර' ලෙස හඳුන්වන නගරය කුමක්ද?",
                "a": "කොළඹ",
                "b": "මහනුවර",
                "c": "ගාල්ල",
                "d": "අනුරාධපුර",
                "correct": "මහනුවර",
                "speak": "mahanuwara"
            },
            {
                "question": "සාම්ප්‍රදායික ශ්‍රී ලාංකික නර්තන නාට්‍යය හඳුන්වන්නේ කුමක්ද?",
                "a": "කතකලි",
                "b": "භරතනාට්‍යය",
                "c": "කොහොඹ කංකාරිය",
                "d": "යක්ෂ ගණ",
                "correct": "කොහොඹ කංකාරිය",
                "speak": "kohoma kankariya"
            },
            {
                "question": "සුප්‍රසිද්ධ ශ්‍රී ලාංකික වෙස් නැටුම් ආකෘතිය හඳුන්වන්නේ කුමක්ද?",
                "a": "උඩරට නර්තනය",
                "b": "කෝලම්",
                "c": "භරතනාට්‍යය",
                "d": "ඔඩිසි",
                "correct": "කෝලම්",
                "speak": "kolam"
            },
            {
                "question": "අලි පෙරහැර සහ ගිනි නැටුම් සමඟ සමරනු ලබන ශ්‍රී ලංකාවේ කුමන උත්සවයද?",
                "a": "දීවාලි",
                "b": "වෙසක්",
                "c": "ඇසළ පෙරහැර",
                "d": "අවුරුදු",
                "correct": "ඇසළ පෙරහැර",
                "speak": "asala perahara"
            },
            {
                "question": "ශ්‍රී ලංකාවට බටහිර දෙසින් පිහිටි ජල කඳ කුමක්ද?",
                "a": "බෙංගාල බොක්ක",
                "b": "අරාබි මුහුද",
                "c": "ඉන්දියන් සාගරය",
                "d": "Lacadive මුහුද",
                "correct": "ඉන්දියන් සාගරය",
                "speak": "indidayan sagaraya"
            },
            {
                "question": "ලන්දේසි යටත් විජිත ගෘහනිර්මාණ ශිල්පය සඳහා ප්‍රසිද්ධ ශ්‍රී ලංකා නගරය කුමක්ද?",
                "a": "කොළඹ",
                "b": "මහනුවර",
                "c": "ගාල්ල",
                "d": "යාපනය",
                "correct": "ගාල්ල",
                "speak": "galla"
            },
            {
                "question": "සාම්ප්‍රදායික ශ්‍රී ලාංකික බත් සහ ව්‍යංජන ආහාරයේ නම කුමක්ද?",
                "a": "බුරියානි",
                "b": "පුලාඕ",
                "c": "ලම්ප්රයිස්",
                "d": "කොත්තු",
                "correct": "ලම්ප්රයිස්",
                "speak": "lampraise"
            },
            {
                "question": "ශ්‍රී ලංකාවේ බෞද්ධ ලෙන්ට් අවසානය සනිටුහන් කරන උත්සවය කුමක්ද?",
                "a": "අවුරුදු",
                "b": "පෝය",
                "c": "වෙසක්",
                "d": "පොසොන්",
                "correct": "පොසොන්",
                "speak": "poson"
            },
            {
                "question": "උඩරට උත්සවයේදී ඉදිරිපත් කරන ශ්‍රී ලාංකික නර්තනය කුමක්ද?",
                "a": "භරතනාට්‍යය",
                "b": "කතක්",
                "c": "වෙස් නැටුම්",
                "d": "යක්ෂ ගණ",
                "correct": "වෙස් නැටුම්",
                "speak": "wes natum"
            },
            {
                "question": "ජන සංගීතයේ භාවිතා වන සාම්ප්‍රදායික ශ්‍රී ලාංකික බෙරයේ නම කුමක්ද?",
                "a": "තබ්ලා",
                "b": "තම්මට්ටම",
                "c": "ඩිජෙම්බේ",
                "d": "මෘදංගම්",
                "correct": "තම්මට්ටම",
                "speak": "thammattama"
            },
            {
                "question": "පහන් කූඩු සහ තොරණ සමඟ සමරනු ලබන ශ්‍රී ලංකාවේ කුමන උත්සවයද?",
                "a": "දීවාලි",
                "b": "වෙසක්",
                "c": "අවුරුදු",
                "d": "නත්තල්",
                "correct": "වෙසක්",
                "speak": "wesak"
            },
            {
                "question": "ශ්‍රී ලාංකේය සම්ප්‍රදායික සුව කිරීමේ ක්‍රමයේ නම කුමක්ද?",
                "a": "ආයුර්වේදය",
                "b": "හෝමියෝපති",
                "c": "ස්වභාවික චිකිත්සාව",
                "d": "කටු චිකිත්සාව",
                "correct": "ආයුර්වේදය",
                "speak": "ayurwedaya"
            },
            {
                "question": "‘මඩොල් දූවා’ නවකතාව ලිව්වේ කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ගුණදාස අමරසේකර",
                "c": "එදිරිවීර සරච්චන්ද්‍ර",
                "d": "ටී බී ඉලංගරත්න",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "‘විරාගය’ කතුවරයා කවුද?",
                "a": "ඩබ්ලිව් ඒ සිල්වා",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "එදිරිවීර සරච්චන්ද්‍ර",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "කුමාරතුංග මුනිදාසයන් විසින් රචිත සිංහල සාහිත්‍යයේ ශ්‍රේෂ්ඨතම කෘතියක් ලෙස සැලකෙන ග්‍රන්ථය කුමක්ද?",
                "a": "කොග්ගල",
                "b": "කුමුදුනී",
                "c": "වෙස්සන්තර",
                "d": "පුජාවලිය",
                "correct": "කොග්ගල",
                "speak": "koggala"
            },
            {
                "question": "යුගාන්තය සිංහල නවකතාව ලිව්වේ කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ගුණදාස අමරසේකර",
                "c": "එදිරිවීර සරච්චන්ද්‍ර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "'ගම්පෙරළිය' කෘතියෙන් ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකේය ලේඛකයා කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "එදිරිවීර සරච්චන්ද්‍ර",
                "c": "ගුණදාස අමරසේකර",
                "d": "ඩබ්ලිව් ඒ සිල්වා",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "‘අපේ ගම’ ලිව්වේ කවුද?",
                "a": "ඩබ්ලිව් ඒ සිල්වා",
                "b": "එදිරිවීර සරච්චන්ද්‍ර",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "‘මනමේ’ ලියූ ශ්‍රී ලාංකික නාට්‍යකරු කවුද?",
                "a": "සරච්චන්ද්‍ර",
                "b": "කුමාරතුංග මුනිදාස",
                "c": "මාර්ටින් වික්‍රමසිංහ",
                "d": "ඩබ්ලිව් ඒ සිල්වා",
                "correct": "සරච්චන්ද්‍ර",
                "speak": "ediriweera sarachchandra"
            },
            {
                "question": "සඳ කිඳුරු කතුවරයා කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ගුණදාස අමරසේකර",
                "c": "කුමාරතුංග මුනිදාස",
                "d": "එදිරිවීර සරච්චන්ද්‍ර",
                "correct": "එදිරිවීර සරච්චන්ද්‍ර",
                "speak": "ediriweera sarachchandra"
            },
            {
                "question": "‘කැලේ හඬ’ නවකතාව ලිව්වේ කවුද?",
                "a": "ඩබ්ලිව් ඒ සිල්වා",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "එදිරිවීර සරච්චන්ද්‍ර",
                "correct": "ඩබ්ලිව් ඒ සිල්වා",
                "speak": "W A silwa"
            },
            {
                "question": "රත්තරං සිංහල නවකතාව ලිව්වේ කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ඩබ්ලිව් ඒ සිල්වා",
                "c": "එදිරිවීර සරච්චන්ද්‍ර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "ඩබ්ලිව් ඒ සිල්වා",
                "speak": "W A silwa"
            },
            {
                "question": "The Way of the Lotus කෘතිය සඳහා ප්‍රසිද්ධියට පත් කතුවරයා කවුද?",
                "a": "කුමාරතුංග මුනිදාස",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "එදිරිවීර සරච්චන්ද්‍ර",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "දොළොස්මහේ පහන එකතුවෙන් ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකේය කවියා කවුද?",
                "a": "එදිරිවීර සරච්චන්ද්‍ර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "මහගම සේකර",
                "correct": "මහගම සේකර",
                "speak": "mahagama sekara"
            },
            {
                "question": "‘බඹරු ඇවිත්’ නවකතාව සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික ලේඛකයා කවුද?",
                "a": "ගුණදාස අමරසේකර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "එදිරිවීර සරච්චන්ද්‍ර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "ගුණදාස අමරසේකර",
                "speak": "gunadasa amarasekara"
            },
            {
                "question": "ඔහු යාපනයෙන් පැමිණි කෘතියේ කතුවරයා කවුද?",
                "a": "සරච්චන්ද්‍ර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "කුමාරතුංග මුනිදාස",
                "d": "සිවගුරුනාදන්",
                "correct": "සරච්චන්ද්‍ර",
                "speak": "ediriweera sarachchandra"
            },
            {
                "question": "'The Water Diviner' කෙටිකතා එකතුව ලිව්වේ කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "එදිරිවීර සරච්චන්ද්‍ර",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "අරලිය මල් ආරාමයේ කතුවරයා කවුද?",
                "a": "එදිරිවීර සරච්චන්ද්‍ර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "එදිරිවීර සරච්චන්ද්‍ර",
                "speak": "ediriweera sarachchandra"
            },
            {
                "question": "‘දහසක් සිතුවිලි’ නවකතාව ලිව්වේ කවුද?",
                "a": "ගුණදාස අමරසේකර",
                "b": "එදිරිවීර සරච්චන්ද්‍ර",
                "c": "මාර්ටින් වික්‍රමසිංහ",
                "d": "ඩබ්ලිව් ඒ සිල්වා",
                "correct": "ගුණදාස අමරසේකර",
                "speak": "gunadasa amarasekara"
            },
            {
                "question": "'හත්පන' කෘතියෙන් ප්‍රකට ශ්‍රී ලාංකේය කවියා කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ඩබ්ලිව් ඒ සිල්වා",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "කුමාරතුංග මුනිදාස",
                "speak": "kumarathunga munidasa"
            },
            {
                "question": "'විරාගය' ලියූ ශ්‍රී ලාංකික කතුවරයා කවුද?",
                "a": "එදිරිවීර සරච්චන්ද්‍ර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "කොග්ගල සිංහල නවකතාව ලිව්වේ කවුද?",
                "a": "කුමාරතුංග මුනිදාස",
                "b": "එදිරිවීර සරච්චන්ද්‍ර",
                "c": "මාර්ටින් වික්‍රමසිංහ",
                "d": "ගුණදාස අමරසේකර",
                "correct": "කුමාරතුංග මුනිදාස",
                "speak": "kumarathunga munidasa"
            },
            {
                "question": "සුප්‍රසිද්ධ ‘ගොළු හදවත’ කෘතියේ කතුවරයා කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ඩබ්ලිව් ඒ සිල්වා",
                "c": "කුමාරතුංග මුනිදාස",
                "d": "කරුණාසේන ජයලත්",
                "correct": "කරුණාසේන ජයලත්",
                "speak": "karunasena jayalath"
            },
            {
                "question": "'ගැහැණු ළමයි' නවකතාව සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික ලේඛකයා කවුද?",
                "a": "මාර්ටින් වික්‍රමසිංහ",
                "b": "ගුණදාස අමරසේකර",
                "c": "කුමාරතුංග මුනිදාස",
                "d": "කරුණාසේන ජයලත්",
                "correct": "කරුණාසේන ජයලත්",
                "speak": "karunasena jayalath"
            },
            {
                "question": "‘අපේ ගම’ කතුවරයා කවුද?",
                "a": "එදිරිවීර සරච්චන්ද්‍ර",
                "b": "මාර්ටින් වික්‍රමසිංහ",
                "c": "ගුණදාස අමරසේකර",
                "d": "කුමාරතුංග මුනිදාස",
                "correct": "මාර්ටින් වික්‍රමසිංහ",
                "speak": "martin wikramasinghe"
            },
            {
                "question": "ජංගම සන්නිවේදනයේ නව්‍යකරණයන් සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "මොබිටෙල්",
                "b": "Dialog Axiata",
                "c": "ශ්‍රී ලංකා ටෙලිකොම්",
                "d": "හච්",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "ශ්‍රී ලංකාව අභ්‍යවකාශ ගත කළ පළමු චන්ද්‍රිකාවේ නම කුමක්ද?",
                "a": "රාවණා-1",
                "b": "ශක්ති-1",
                "c": "ලංකාසැට්",
                "d": "සත්‍ය-1",
                "correct": "රාවණා-1",
                "speak": "rawana 1"
            },
            {
                "question": "ප්‍රබල ඉංජිනේරු සහ තාක්‍ෂණ වැඩසටහන් සඳහා ප්‍රසිද්ධ ශ්‍රී ලංකාවේ කුමන විශ්වවිද්‍යාලයද?",
                "a": "කොළඹ විශ්වවිද්‍යාලය",
                "b": "පේරාදෙණිය විශ්වවිද්‍යාලය",
                "c": "මොරටුව විශ්වවිද්‍යාලය",
                "d": "යාපනය විශ්වවිද්‍යාලය",
                "correct": "මොරටුව විශ්වවිද්‍යාලය",
                "speak": "moratuwa wishwawidyalaya"
            },
            {
                "question": "ශ්‍රී ලංකාවේ WSO2 මෘදුකාංග සමාගමේ නිර්මාතෘ කවුද?",
                "a": "සංජීව වීරවරණ",
                "b": "හර්ෂ පුරසිංහ",
                "c": "මදු රත්නායක",
                "d": "සුරේන් අමරසේකර",
                "correct": "සංජීව වීරවරණ",
                "speak": "sanjeewa weerawarana"
            },
            {
                "question": "ශ්‍රී ලාංකේය තාක්ෂණික සමාගමක් වන hSenid හි ප්‍රධාන අවධානය කුමක්ද?",
                "a": "විදුලි සංදේශ",
                "b": "ඊ-වාණිජ්යය",
                "c": "මානව සම්පත් විසඳුම්",
                "d": "කෘතිම බුද්ධිය",
                "correct": "මානව සම්පත් විසඳුම්",
                "speak": "manawa sampath wisadum"
            },
            {
                "question": "'ශ්‍රී ලංකාවේ සිලිකන් නිම්නය' ලෙස හඳුන්වන ශ්‍රී ලංකා නගරය කුමක්ද?",
                "a": "කොළඹ",
                "b": "මහනුවර",
                "c": "යාපනය",
                "d": "මොරටුව",
                "correct": "මොරටුව",
                "speak": "moratuwa"
            },
            {
                "question": "PickMe යෙදුම නිපදවූ ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "Dialog Axiata",
                "b": "hSenid",
                "c": "PickMe Lanka",
                "d": "කප්රුක",
                "correct": "PickMe Lanka",
                "speak": "PickMe Lanka"
            },
            {
                "question": "ශ්‍රී ලංකාවේ මාලඹේ පිහිටි තාක්ෂණික උද්‍යානය කුමක්ද?",
                "a": "ට්‍රේස් සිටි",
                "b": "ඔරියන් නගරය",
                "c": "තාක්ෂණික නගරය",
                "d": "පාර්ක් සිටි",
                "correct": "ට්‍රේස් සිටි",
                "speak": "trace city"
            },
            {
                "question": "ශ්‍රී ලංකාවේ ප්‍රථම තොරතුරු තාක්ෂණ උපාධි පිරිනමන ආයතනයේ නම කුමක්ද?",
                "a": "SLIIT",
                "b": "NSBM හරිත විශ්ව විද්‍යාලය",
                "c": "කොළඹ විශ්වවිද්‍යාලයේ පරිගණක පාසල",
                "d": "ESOFT මෙට්‍රෝ කැම්පස්",
                "correct": "SLIIT",
                "speak": "SLIIT"
            },
            {
                "question": "ඊ-වාණිජ්‍ය වේදිකාව සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකේය තාක්ෂණික සමාගම කුමක්ද?",
                "a": "කප්රුක",
                "b": "WSO2",
                "c": "hSenid",
                "d": "MillenniumIT",
                "correct": "කප්රුක",
                "speak": "kapruka"
            },
            {
                "question": "කප්රුක නම් ඊ-වාණිජ්‍යය සමාගමේ නිර්මාතෘ කවුද?",
                "a": "සංජීව වීරවරණ",
                "b": "දුලිත් හේරත්",
                "c": "හර්ෂ පුරසිංහ",
                "d": "අශාන්ති කෝරලගේ",
                "correct": "දුලිත් හේරත්",
                "speak": "dulith herath"
            },
            {
                "question": "කොටස් හුවමාරු තාක්ෂණික විසඳුම් පිළිබඳ විශේෂඥතාව ඇති ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "WSO2",
                "b": "MillenniumIT",
                "c": "Dialog Axiata",
                "d": "මොබිටෙල්",
                "correct": "MillenniumIT",
                "speak": "Millennium IT"
            },
            {
                "question": "ශ්‍රී ලංකාවේ තොරතුරු හා සන්නිවේදන තාක්ෂණයේ දියුණුව සඳහා වගකිව යුතු සංවිධානය කුමක්ද?",
                "a": "ICTA",
                "b": "SLASSCOM",
                "c": "ශ්‍රී ලංකා ටෙලිකොම්",
                "d": "TRCSL",
                "correct": "ICTA",
                "speak": "ICTA"
            },
            {
                "question": "cloud මත පදනම් වූ මානව සම්පත් විසඳුම් සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "WSO2",
                "b": "hSenid",
                "c": "MillenniumIT",
                "d": "කප්රුක",
                "correct": "hSenid",
                "speak": "hSenid"
            },
            {
                "question": "'ඩිජිටල් ශ්‍රී ලංකා' වැඩසටහනේ ප්‍රධාන අරමුණ කුමක්ද?",
                "a": "ඊ-වාණිජ්‍යය වැඩිදියුණු කිරීමට",
                "b": "අන්තර්ජාල සම්බන්ධතාව වැඩිදියුණු කිරීමට",
                "c": "රජයේ සේවාවන් ඩිජිටල්කරණය කිරීමට",
                "d": "තාක්ෂණික ආරම්භයන් ප්රවර්ධනය කිරීම සඳහා",
                "correct": "රජයේ සේවාවන් ඩිජිටල්කරණය කිරීමට",
                "speak": "rajaye sewawan digitalkaranaya kirima"
            },
            {
                "question": "මෙකට්‍රොනික්ස් ඉංජිනේරු විද්‍යාව පිළිබඳ විශේෂිත උපාධියක් පිරිනමන ශ්‍රී ලංකාවේ කුමන විශ්වවිද්‍යාලයද?",
                "a": "පේරාදෙණිය විශ්වවිද්‍යාලය",
                "b": "මොරටුව විශ්වවිද්‍යාලය",
                "c": "කොළඹ විශ්වවිද්‍යාලය",
                "d": "යාපනය විශ්වවිද්‍යාලය",
                "correct": "මොරටුව විශ්වවිද්‍යාලය",
                "speak": "moratuwa wishwawidyalaya"
            },
            {
                "question": "සබැඳි ගෙවීම් ද්වාර විසඳුම් සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික තාක්ෂණික ආරම්භය කුමක්ද?",
                "a": "hSenid",
                "b": "PayHere",
                "c": "WSO2",
                "d": "PickMe",
                "correct": "PayHere",
                "speak": "Pay Here"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පළමු 4G LTE ජාලය දියත් කළේ කුමන ජංගම දුරකථන ක්‍රියාකරුද?",
                "a": "මොබිටෙල්",
                "b": "Dialog Axiata",
                "c": "හච්",
                "d": "ශ්‍රී ලංකා ටෙලිකොම්",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "ශ්‍රී ලංකාවේ විශාලතම තොරතුරු තාක්ෂණ සමුළුව ලෙස සැලකෙන්නේ කුමන තාක්ෂණික ඉසව්ව ද?",
                "a": "SLASSCOM තාක්ෂණික සමුළුව",
                "b": "Disrupt Asia",
                "c": "ඉන්ෆොටෙල්",
                "d": "Echelon",
                "correct": "Disrupt Asia",
                "speak": "Disrupt Asia"
            },
            {
                "question": "කොළඹ පිහිටි ‘Trace Expert City’ හි අවධානය කුමක් ද?",
                "a": "ඊ-වාණිජ්යය",
                "b": "මෘදුකාංග සංවර්ධනය",
                "c": "Startups and Innovation",
                "d": "විදුලි සංදේශ",
                "correct": "Startups and Innovation",
                "speak": "Startups and Innovation"
            },
            {
                "question": "ලොව පුරා කොටස් හුවමාරු සඳහා ප්‍රාග්ධන වෙළෙඳපොළ මෘදුකාංග සපයන ශ්‍රී ලාංකික තාක්ෂණික සමාගම කුමක්ද?",
                "a": "MillenniumIT",
                "b": "WSO2",
                "c": "hSenid",
                "d": "මෙහි ගෙවන්න",
                "correct": "MillenniumIT",
                "speak": "Millennium IT"
            },
            {
                "question": "Dialog Axiata හි මූලස්ථානයට සත්කාරකත්වය සපයන ශ්‍රී ලංකාවේ කුමන නගරයද?",
                "a": "මහනුවර",
                "b": "කොළඹ",
                "c": "ගාල්ල",
                "d": "යාපනය",
                "correct": "කොළඹ",
                "speak": "kolaba"
            },
            {
                "question": "නිවාස තාක්ෂණික ආරම්භක සහ නවෝත්පාදන මධ්‍යස්ථාන සඳහා ප්‍රසිද්ධ කොළඹ කුමන තාක්ෂණික උද්‍යානයද?",
                "a": "ඔරියන් නගරය",
                "b": "තාක්ෂණික නගරය",
                "c": "පාර්ක් සිටි",
                "d": "ට්‍රේස් සිටි",
                "correct": "ඔරියන් නගරය",
                "speak": "oriyan nagaraya"
            },
            {
                "question": "පොදු ප්‍රවාහනය සඳහා ඉලෙක්ට්‍රොනික ප්‍රවේශපත්‍ර ක්‍රමය සංවර්ධනය කිරීම සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "MillenniumIT",
                "b": "Dialog Axiata",
                "c": "hSenid",
                "d": "ශ්‍රී ලංකා ටෙලිකොම්",
                "correct": "Dialog Axiata",
                "speak": "Dialog Axiata"
            },
            {
                "question": "ශ්‍රී ලංකාවේ තාක්ෂණික සමාගම වන MillenniumIT හි නිර්මාතෘ කවුද?",
                "a": "ටෝනි වීරසිංහ",
                "b": "සංජීව වීරවරණ",
                "c": "හර්ෂ පුරසිංහ",
                "d": "දුලිත් හේරත්",
                "correct": "ටෝනි වීරසිංහ",
                "speak": "tony weerasinghe"
            },
            {
                "question": "විවෘත මූලාශ්‍ර මිඩ්ල්වෙයාර් විසඳුම් පිළිබඳ විශේෂඥතාව ඇති ශ්‍රී ලාංකික සමාගම කුමක්ද?",
                "a": "hSenid",
                "b": "MillenniumIT",
                "c": "WSO2",
                "d": "Dialog Axiata",
                "correct": "WSO2",
                "speak": "W S O deka"
            },
            {
                "question": "ඔන්ලයින් සිල්ලර බඩු බෙදා හැරීමේ සේවාවන්හි පුරෝගාමියා වන ශ්‍රී ලාංකික තාක්ෂණික සමාගම කුමක්ද?",
                "a": "කප්රුක",
                "b": "pick Me",
                "c": "WSO2",
                "d": "hSenid",
                "correct": "කප්රුක",
                "speak": "kapruka"
            },
            {
                "question": "තොරතුරු තාක්ෂණ සඳහා කැපවූ පීඨයක් ඇති ශ්‍රී ලංකාවේ කුමන විශ්ව විද්‍යාලයද?",
                "a": "කොළඹ විශ්වවිද්‍යාලය",
                "b": "පේරාදෙණිය විශ්වවිද්‍යාලය",
                "c": "මොරටුව විශ්වවිද්‍යාලය",
                "d": "රුහුණු විශ්වවිද්‍යාලය",
                "correct": "මොරටුව විශ්වවිද්‍යාලය",
                "speak": "moratuwa wishwawidyalaya"
            },
            {
                "question": "ශ්‍රී ලංකා ඉතිහාසයේ විශිෂ්ඨතම ක්‍රිකට් ක්‍රීඩකයෙකු ලෙස සැලකෙන සහ ටෙස්ට් ක්‍රිකට් පිටියේ ඉදිරියෙන්ම සිටින කඩුලු ලාභියා කවුද?",
                "a": "අර්ජුන රණතුංග",
                "b": "සනත් ජයසූරිය",
                "c": "කුමාර සංගක්කාර",
                "d": "මුත්තයියා මුරලිදරන්",
                "correct": "මුත්තයියා මුරලිදරන්",
                "speak": "muththaiya muralidaran"
            },
            {
                "question": "ටෙස්ට් තරගයකදී ලකුණු 374ක් රැස්කළ ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා, එය ශ්‍රී ලාංකිකයෙකු විසින් ලබාගත් වැඩිම පුද්ගලික ලකුණු සංඛ්‍යාවද?",
                "a": "කුමාර සංගක්කාර",
                "b": "මහේල ජයවර්ධන",
                "c": "සනත් ජයසූරිය",
                "d": "අරවින්ද ද සිල්වා",
                "correct": "මහේල ජයවර්ධන",
                "speak": "mahela jayawardhan"
            },
            {
                "question": "1996 දී ශ්‍රී ලංකා ක්‍රිකට් කණ්ඩායමේ පළමු සහ එකම ICC ක්‍රිකට් ලෝක කුසලාන ජයග්‍රහණය කරා මෙහෙයවූයේ කවුද?",
                "a": "අර්ජුන රණතුංග",
                "b": "සනත් ජයසූරිය",
                "c": "කුමාර සංගක්කාර",
                "d": "මාවන් අතපත්තු",
                "correct": "අර්ජුන රණතුංග",
                "speak": "arjuna ranathunga"
            },
            {
                "question": "2000 සිඩ්නි ඔලිම්පික් උළෙලේදී මීටර් 200 රිදී පදක්කමක් දිනූ ශ්‍රී ලංකා කෙටි දුර ධාවන ක්‍රීඩකයා කවුද?",
                "a": "සුසන්තිකා ජයසිංහ",
                "b": "ඩන්කන් වයිට්",
                "c": "නිම්මි ද සිල්වා",
                "d": "සුගත් තිලකරත්න",
                "correct": "සුසන්තිකා ජයසිංහ",
                "speak": "susanthika jayasinghe"
            },
            {
                "question": "ශ්‍රී ලංකාවේ ජාතික ක්‍රීඩාව ලෙස බහුලව සැලකෙන්නේ කුමන ක්‍රීඩාවද?",
                "a": "ක්රිකට්",
                "b": "වොලිබෝල්",
                "c": "රග්බි",
                "d": "පාපන්දු",
                "correct": "වොලිබෝල්",
                "speak": "wolly ball"
            },
            {
                "question": "ඔලිම්පික් උළෙලේ පදක්කමක් දිනූ පළමු ශ්‍රී ලාංකිකයා කවුද?",
                "a": "සුසන්තිකා ජයසිංහ",
                "b": "ඩන්කන් වයිට්",
                "c": "නිම්මි ද සිල්වා",
                "d": "සුගත් තිලකරත්න",
                "correct": "ඩන්කන් වයිට්",
                "speak": "dunkan white"
            },
            {
                "question": "එක්දින ක්‍රිකට් ක්‍රීඩාවේ වේගවත්ම අර්ධ ශතකයේ වාර්තාවට හිමිකම් කියන ශ්‍රී ලංකා ක්‍රීඩකයා කවුද?",
                "a": "සනත් ජයසූරිය",
                "b": "කුමාර සංගක්කාර",
                "c": "තිලකරත්න ඩිල්ෂාන්",
                "d": "තිසර පෙරේරා",
                "correct": "සනත් ජයසූරිය",
                "speak": "sanath jayasuriya"
            },
            {
                "question": "ටෙස්ට් ක්‍රිකට් පිටියේ ලකුණු 10,000 රැස් කළ පළමු ශ්‍රී ලංකා ක්‍රීඩකයා කවුද?",
                "a": "මහේල ජයවර්ධන",
                "b": "කුමාර සංගක්කාර",
                "c": "සනත් ජයසූරිය",
                "d": "අරවින්ද ද සිල්වා",
                "correct": "කුමාර සංගක්කාර",
                "speak": "kumarathunga munidasa"
            },
            {
                "question": "දකුණු ආසියානු ක්‍රීඩා උළෙලේදී උස පැනීමේ ජයග්‍රහණ සඳහා ප්‍රසිද්ධ සහ පදක්කම් කිහිපයක් දිනාගෙන ඇති ශ්‍රී ලංකා ක්‍රීඩිකාව කවුද?",
                "a": "නිම්මි ද සිල්වා",
                "b": "ඩන්කන් වයිට්",
                "c": "සුසන්තිකා ජයසිංහ",
                "d": "සුගත් තිලකරත්න",
                "correct": "නිම්මි ද සිල්වා",
                "speak": "nimmi the silva"
            },
            {
                "question": "'ඩිල්ස්කූප්' වෙඩිල්ල නිර්මාණය කිරීම සම්බන්ධයෙන් ප්‍රසිද්ධ ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා කවුද?",
                "a": "මහේල ජයවර්ධන",
                "b": "සනත් ජයසූරිය",
                "c": "තිලකරත්න ඩිල්ෂාන්",
                "d": "අරවින්ද ද සිල්වා",
                "correct": "තිලකරත්න ඩිල්ෂාන්",
                "speak": "thilakarathne dilshan"
            },
            {
                "question": "ඉන්දීය ප්‍රිමියර් ලීගයට (IPL) ක්‍රීඩා කළ පළමු ශ්‍රී ලාංකිකයා කවුද?",
                "a": "සනත් ජයසූරිය",
                "b": "මුත්තයියා මුරලිදරන්",
                "c": "කුමාර සංගක්කාර",
                "d": "මහේල ජයවර්ධන",
                "correct": "සනත් ජයසූරිය",
                "speak": "sanath jayasuriya"
            },
            {
                "question": "ඔහුගේ අසාමාන්‍ය පන්දු යැවීමේ ඉරියව්ව සඳහා ප්‍රසිද්ධියට පත් වූ ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා කවුද?",
                "a": "මුත්තයියා මුරලිදරන්",
                "b": "ලසිත් මාලිංග",
                "c": "අජන්ත මෙන්ඩිස්",
                "d": "සචිත්‍ර සේනානායක",
                "correct": "මුත්තයියා මුරලිදරන්",
                "speak": "muththaiya muralidaran"
            },
            {
                "question": "1950 බ්‍රිතාන්‍ය එම්පයර් ක්‍රීඩා උළෙලේදී ලෝකඩ පදක්කමක් දිනූ ශ්‍රී ලාංකික බොක්සිං ක්‍රීඩකයා කවුද?",
                "a": "ඩන්කන් වයිට්",
                "b": "එඩී ග්‍රේ",
                "c": "එච්.කේ කරුණාරත්න",
                "d": "කේපී එඩ්වින්",
                "correct": "එඩී ග්‍රේ",
                "speak": "eddy gray"
            },
            {
                "question": "ලෝක කුසලාන තරගයකදී කඩුලු ත්‍රිත්වයක් ලබාගත් පළමු ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා කවුද?",
                "a": "ලසිත් මාලිංග",
                "b": "චමින්ද වාස්",
                "c": "අජන්ත මෙන්ඩිස්",
                "d": "නුවන් කුලසේකර",
                "correct": "චමින්ද වාස්",
                "speak": "chaminda vas"
            },
            {
                "question": "කඩුලු රකින්නෙකු නොවන ටෙස්ට් ක්‍රිකට් ක්‍රීඩාවේ වැඩිම උඩ පන්දු රැකීමේ වාර්තාවට හිමිකම් කියන ශ්‍රී ලංකා ක්‍රීඩකයා කවුද?",
                "a": "කුමාර සංගක්කාර",
                "b": "මහේල ජයවර්ධන",
                "c": "සනත් ජයසූරිය",
                "d": "අරවින්ද ද සිල්වා",
                "correct": "මහේල ජයවර්ධන",
                "speak": "mahela jayawardhana"
            },
            {
                "question": "කැපී පෙනෙන පන්දු යැවීමේ ඉරියව්ව සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා සහ විශිෂ්ටතම T20 පන්දු යවන්නෙක් කවුද?",
                "a": "ලසිත් මාලිංග",
                "b": "චමින්ද වාස්",
                "c": "නුවන් කුලසේකර",
                "d": "තිසර පෙරේරා",
                "correct": "ලසිත් මාලිංග",
                "speak": "lasith malinga"
            },
            {
                "question": "1998 ආසියානු ක්‍රීඩා උළෙලේ පිරිමි මීටර් 400 කඩුලු මතින් දිවීමේ ඉසව්වේ රන් පදක්කම දිනූ ශ්‍රී ලංකා ක්‍රීඩිකාව කවුද?",
                "a": "සුගත් තිලකරත්න",
                "b": "රොහාන් ප්‍රදීප් කුමාර",
                "c": "ඩන්කන් වයිට්",
                "d": "ශ්‍රියන්ත දිසානායක",
                "correct": "සුගත් තිලකරත්න",
                "speak": "sugath thilakarathne"
            },
            {
                "question": "ටෙස්ට් තරගයකදී ද්විත්ව ශතකයක් ලබාගත් පළමු ශ්‍රී ලංකා ක්‍රිකට් ක්‍රීඩකයා කවුද?",
                "a": "සනත් ජයසූරිය",
                "b": "අරවින්ද ද සිල්වා",
                "c": "කුමාර සංගක්කාර",
                "d": "මහේල ජයවර්ධන",
                "correct": "සනත් ජයසූරිය",
                "speak": "sanath jayasuriya"
            },
            {
                "question": "එක්දින ක්‍රිකට් පිටියේ වේගවත්ම ලකුණු 150 රැස් කළ ශ්‍රී ලාංකික ක්‍රීඩකයා කවුද?",
                "a": "සනත් ජයසූරිය",
                "b": "කුමාර සංගක්කාර",
                "c": "තිලකරත්න ඩිල්ෂාන්",
                "d": "තිසර පෙරේරා",
                "correct": "සනත් ජයසූරිය",
                "speak": "sanath jayasuriya"
            },
            {
                "question": "ඔලිම්පික් ක්‍රීඩා උළෙලට සහභාගී වූ පළමු ශ්‍රී ලාංකික ක්‍රීඩිකාව කවුද?",
                "a": "සුසන්තිකා ජයසිංහ",
                "b": "නිම්මි ද සිල්වා",
                "c": "දමයන්ති දර්ශා",
                "d": "අනුරාධ කුරේ",
                "correct": "දමයන්ති දර්ශා",
                "speak": "diayamanthi darsha"
            },
            {
                "question": "ක්ලිෆර්ඩ් කුසලානය වැඩිම වාර ගණනක් දිනූ ශ්‍රී ලංකා රග්බි කණ්ඩායම කුමක්ද?",
                "a": "මහනුවර එස්.සී",
                "b": "හැව්ලොක් එස්.සී",
                "c": "CR & FC",
                "d": "නාවික එස්.සී",
                "correct": "මහනුවර එස්.සී",
                "speak": "mahanuwara S C"
            },
            {
                "question": "ටෙස්ට් ක්‍රිකට් ක්‍රීඩාවේදී කුමාර් සංගක්කාර සමඟ වාර්තාගත සබඳතාවයකට ප්‍රසිද්ධියට පත් ශ්‍රී ලංකා ක්‍රීඩකයා කවුද?",
                "a": "මහේල ජයවර්ධන",
                "b": "සනත් ජයසූරිය",
                "c": "තිලකරත්න ඩිල්ෂාන්",
                "d": "අර්ජුන රණතුංග",
                "correct": "මහේල ජයවර්ධන",
                "speak": "Mahela ajayawardhane"
            },
            {
                "question": "2011 ICC ක්‍රිකට් ලෝක කුසලානයේදී ශ්‍රී ලංකා ක්‍රිකට් කණ්ඩායමේ නායකයා කවුද?",
                "a": "සනත් ජයසූරිය",
                "b": "මහේල ජයවර්ධන",
                "c": "කුමාර සංගක්කාර",
                "d": "ඇන්ජලෝ මැතිව්ස්",
                "correct": "කුමාර සංගක්කාර",
                "speak": "kumara sangakkara"
            },
            {
                "question": "නිදහස් ශ්‍රී ලංකාවේ පළමු අග්‍රාමාත්‍යවරයා කවුද?",
                "a": "ජේ ආර් ජයවර්ධන",
                "b": "SWRD බණ්ඩාරනායක",
                "c": "ඩී.එස්.සේනානායක",
                "d": "සර් ජෝන් කොතලාවල",
                "correct": "ඩී.එස්.සේනානායක",
                "speak": "D S Senanayake"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පැරණි නම කුමක්ද?",
                "a": "ටැප්රොබේන්",
                "b": "Ceylon",
                "c": "සෙරන්ඩිබ්",
                "d": "Lanka",
                "correct": "Ceylon",
                "speak": "Ceylon"
            },
            {
                "question": "සීගිරි පර්වත බලකොටුව ඉදිකළ ශ්‍රී ලංකාවේ කිනම් රජුද?",
                "a": "කාශ්‍යප රජු",
                "b": "දුටුගැමුණු රජතුමා",
                "c": "පරාක්‍රමබාහු රජතුමා",
                "d": "මහසෙන් රජතුමා",
                "correct": "කාශ්‍යප රජු",
                "speak": "kashyapa raju"
            },
            {
                "question": "උඩරට රාජධානියේ නිර්මාතෘ කවුද?",
                "a": "පළමුවන විජයබාහු රජු",
                "b": "සෙනරත් රජු",
                "c": "I විමලධර්මසූරිය රජු",
                "d": "I රාජසිංහ රජු",
                "correct": "I විමලධර්මසූරිය රජු",
                "speak": "palamuwana wimaladarmasuriya raju"
            },
            {
                "question": "16 වැනි සියවසේදී ශ්‍රී ලංකාව ප්‍රථමයෙන් අත්පත් කරගත් යටත්විජිත බලය කුමක්ද?",
                "a": "පෘතුගීසි",
                "b": "ලන්දේසි",
                "c": "බ්රිතාන්ය",
                "d": "ප්රංශ",
                "correct": "පෘතුගීසි",
                "speak": "pruthugisi"
            },
            {
                "question": "ශ්‍රී ලංකාවේ අවසන් රජු කවුද?",
                "a": "දෙවන රාජසිංහ රජු",
                "b": "හයවන බුවනෙකබාහු රජු",
                "c": "ශ්‍රී වික්‍රම රාජසිංහ රජතුමා",
                "d": "ධර්මපාල රජතුමා",
                "correct": "ශ්‍රී වික්‍රම රාජසිංහ රජතුමා",
                "speak": "sri wikrama rajasinghe rajathuma"
            },
            {
                "question": "බ්‍රිතාන්‍ය පාලනයෙන් ශ්‍රී ලංකාව නිදහස ලැබුවේ කුමන වර්ෂයේදීද?",
                "a": "1948",
                "b": "1950",
                "c": "1947",
                "d": "1952",
                "correct": "1948",
                "speak": "ekdahas nawasiya hathalis ata"
            },
            {
                "question": "අනුරාධපුර රාජධානියේ පැරණි අගනුවර කුමක්ද?",
                "a": "මහනුවර",
                "b": "පොළොන්නරුව",
                "c": "අනුරාධපුර",
                "d": "සීගිරිය",
                "correct": "අනුරාධපුර",
                "speak": "anuradhapuraya"
            },
            {
                "question": "1971 ජවිපෙ කැරැල්ලේ නායකයා කවුද?",
                "a": "රෝහණ විජේවීර",
                "b": "සෝමවංශ අමරසිංහ",
                "c": "විජේවීර ගුණරත්න",
                "d": "අනුර කුමාර දිසානායක",
                "correct": "රෝහණ විජේවීර",
                "speak": "rohana wijeweera"
            },
            {
                "question": "චෝල ආක්‍රමණිකයන් පරාජය කිරීම සම්බන්ධයෙන් ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික රජු කවුද?",
                "a": "පළමුවන විජයබාහු රජු",
                "b": "I පරාක්‍රමබාහු රජතුමා",
                "c": "දුටුගැමුණු රජතුමා",
                "d": "I බුවනෙකබාහු රජු",
                "correct": "පළමුවන විජයබාහු රජු",
                "speak": "palamuwana wiyayabahu raju"
            },
            {
                "question": "ශ්‍රී ලංකාවේ දකුණේ පිහිටුවන ලද සහ යුරෝපීය යටත් විජිතකරණයට එරෙහි වූ රාජධානිය කුමක්ද?",
                "a": "අනුරාධපුර",
                "b": "පොළොන්නරුව",
                "c": "යාපනය",
                "d": "මහනුවර",
                "correct": "මහනුවර",
                "speak": "mahanuwara"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පළමු ජනාධිපතිවරයා කවුද?",
                "a": "රණසිංහ ප්‍රේමදාස",
                "b": "විලියම් ගොපල්ලව",
                "c": "ජේ ආර් ජයවර්ධන",
                "d": "SWRD බණ්ඩාරනායක",
                "correct": "ජේ ආර් ජයවර්ධන",
                "speak": "J R jayawardhena"
            },
            {
                "question": "පරාක්‍රම සමුද්‍රය ඉදිකිරීම සම්බන්ධයෙන් ප්‍රසිද්ධියට පත්ව ඇත්තේ කුමන රජුද?",
                "a": "පළමුවන විජයබාහු රජු",
                "b": "දුටුගැමුණු රජතුමා",
                "c": "I පරාක්‍රමබාහු රජතුමා",
                "d": "I බුවනෙකබාහු රජු",
                "correct": "I පරාක්‍රමබාහු රජතුමා",
                "speak": "palamuwana parakramabahu rajathuma"
            },
            {
                "question": "අනුරාධපුරයේ පැරණි නම කුමක්ද?",
                "a": "තම්බපන්නි",
                "b": "උපතිස්ස",
                "c": "අනුර",
                "d": "මහගම",
                "correct": "උපතිස්ස",
                "speak": "upathissa"
            },
            {
                "question": "ශ්‍රී ලංකාව පාලනය කළ පළමු සිංහල රජු කවුද?",
                "a": "විජය රජු",
                "b": "පණ්ඩුකාභය රජු",
                "c": "දේවානම්පිය තිස්ස රජතුමා",
                "d": "දුටුගැමුණු රජතුමා",
                "correct": "විජය රජු",
                "speak": "wijaya raju"
            },
            {
                "question": "'නැගෙනහිර ධාන්‍යාගාරය' ලෙස හැඳින්වූ ශ්‍රී ලංකාවේ කුමන නගරයද?",
                "a": "අනුරාධපුර",
                "b": "පොළොන්නරුව",
                "c": "මහනුවර",
                "d": "ගාල්ල",
                "correct": "පොළොන්නරුව",
                "speak": "polonnaruwa"
            },
            {
                "question": "යාපනය රාජධානියේ නිර්මාතෘ කවුද?",
                "a": "සංගිලි රජතුමා",
                "b": "කාලිංග මාඝ රජු",
                "c": "ආර්යචක්‍රවර්ති රජු",
                "d": "පරරාජසේකරම් රජු",
                "correct": "ආර්යචක්‍රවර්ති රජු",
                "speak": "aryachakrawarthi raju"
            },
            {
                "question": "රට තුළ බුදුදහම ප්‍රතිෂ්ඨාපනය කිරීමට ගත් උත්සාහය සම්බන්ධයෙන් ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික රජු කවුද?",
                "a": "දුටුගැමුණු රජතුමා",
                "b": "පළමුවන විජයබාහු රජු",
                "c": "දේවානම්පිය තිස්ස රජතුමා",
                "d": "I පරාක්‍රමබාහු රජතුමා",
                "correct": "දේවානම්පිය තිස්ස රජතුමා",
                "speak": "dewanampiyathissa rajathuma"
            },
            {
                "question": "1658 දී පෘතුගීසීන්ගෙන් ශ්‍රී ලංකාව පාලනය අතට ගත් යුරෝපීය රට කුමක්ද?",
                "a": "ප්‍රංශය",
                "b": "නෙදර්ලන්තය",
                "c": "ස්පාඤ්ඤය",
                "d": "ඩෙන්මාර්කය",
                "correct": "නෙදර්ලන්තය",
                "speak": "netherlanthaya"
            },
            {
                "question": "ශ්‍රී ලංකාවේ පළමු අගමැතිනිය කවුද?",
                "a": "සිරිමාවෝ බණ්ඩාරනායක",
                "b": "චන්ද්‍රිකා කුමාරතුංග",
                "c": "ඉන්දිරා ගාන්ධි",
                "d": "මාග්රට් තැචර්",
                "correct": "සිරිමාවෝ බණ්ඩාරනායක",
                "speak": "sirimawo bandaranayake"
            },
            {
                "question": "විස්තීර්ණ වාරි පද්ධති සඳහා ප්‍රසිද්ධ වූ පැරණි ශ්‍රී ලංකා රාජධානිය කුමක්ද?",
                "a": "මහනුවර",
                "b": "අනුරාධපුර",
                "c": "ගම්පොල",
                "d": "යාපනය",
                "correct": "අනුරාධපුර",
                "speak": "anuradhapuraya"
            },
            {
                "question": "නිදහස් ශ්‍රී ලංකාවේ පළමු ආණ්ඩුකාරවරයා කවුද?",
                "a": "විලියම් ගොපල්ලව",
                "b": "ඩී.එස්.සේනානායක",
                "c": "සර් ඔලිවර් ගුණතිලක",
                "d": "සර් ජෝන් කොතලාවල",
                "correct": "සර් ඔලිවර් ගුණතිලක",
                "speak": "sir oliver gunathilake"
            },
            {
                "question": "පෘතුගීසි යටත් විජිතකරණයට එරෙහි ප්‍රතිරෝධය සඳහා ප්‍රසිද්ධ වූ ශ්‍රී ලංකා රාජධානිය කුමක්ද?",
                "a": "මහනුවර",
                "b": "අනුරාධපුර",
                "c": "පොළොන්නරුව",
                "d": "යාපනය",
                "correct": "මහනුවර",
                "speak": "mahanuwara"
            },
            {
                "question": "බුදුදහම වැළඳගත් පළමු සිංහල රජු කවුද?",
                "a": "විජය රජු",
                "b": "පණ්ඩුකාභය රජු",
                "c": "දේවානම්පිය තිස්ස රජතුමා",
                "d": "දුටුගැමුණු රජතුමා",
                "correct": "දේවානම්පිය තිස්ස රජතුමා",
                "speak": "dewanam piyathissa rajathuma"
            },
            {
                "question": "යුරෝපීය යටත් විජිතවාදීන් ආකර්ෂණය කරගත් පුරාණ ශ්‍රී ලංකාවේ ප්‍රධාන අපනයනය කුමක්ද?",
                "a": "කුළුබඩු",
                "b": "රන්",
                "c": "සේද",
                "d": "තේ",
                "correct": "කුළුබඩු",
                "speak": "kulu badu"
            },
            {
                "question": "ශ්‍රී ලංකා නිදහස් ව්‍යාපාරයේ නායකයා කවුද?",
                "a": "SWRD බණ්ඩාරනායක",
                "b": "ඩී.එස්.සේනානායක",
                "c": "රණසිංහ ප්‍රේමදාස",
                "d": "ජේ ආර් ජයවර්ධන",
                "correct": "ඩී.එස්.සේනානායක",
                "speak": "D S Senanayake"
            },
            {
                "question": "හොඳින් සංරක්ෂණය කර ඇති නටබුන් සඳහා ප්‍රසිද්ධ යුනෙස්කෝ ලෝක උරුම අඩවියක් වන ශ්‍රී ලංකාවේ කුමන පැරණි නගරයද?",
                "a": "මහනුවර",
                "b": "පොළොන්නරුව",
                "c": "යාපනය",
                "d": "කොළඹ",
                "correct": "පොළොන්නරුව",
                "speak": "polonnaruwa"
            },
            {
                "question": "ශ්‍රී ලංකාවේ නවීන වෛද්‍ය විද්‍යාවේ පියා ලෙස හඳුන්වන්නේ කවුද?",
                "a": "Dr. එස්ආර් කෝට්ටේගොඩ",
                "b": "Dr. සී.ජී.ඌරාගොඩ",
                "c": "Dr. පී.බී ප්‍රනාන්දු",
                "d": "Dr. ඒ.ආර්.පෙරේරා",
                "correct": "Dr. පී.බී ප්‍රනාන්දු",
                "speak": "adarya P B Pranadu"
            },
            {
                "question": "විද්‍යා ජ්‍යෝති ගෞරව නාමයෙන් පිදුම් ලැබූ රසායන විද්‍යා ක්ෂේත්‍රයේ ඔහුගේ සේවය සඳහා ප්‍රසිද්ධියට පත් වූ ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. ROB විජේසේකර",
                "speak": "mahacharya ROB wijesekara"
            },
            {
                "question": "Panspermia න්‍යාය සඳහා ඔහුගේ දායකත්වය සම්බන්ධයෙන් ප්‍රසිද්ධ ශ්‍රී ලාංකික තාරකා භෞතික විද්‍යාඥයෙකු කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "පාරිසරික භෞතික විද්‍යාව සහ තිරසාර සංවර්ධනය පිළිබඳ පර්යේෂණ සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික භෞතික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මොහාන් මුණසිංහ",
                "speak": "mahacharya mohon munasinghe"
            },
            {
                "question": "SARS කොරෝනා වයිරසය සොයාගත්තේ කවුද සහ ශ්‍රී ලංකාවේ ප්‍රමුඛ පෙළේ වෛරස් විද්‍යාඥයෙක්ද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මලික් පීරිස්",
                "speak": "mahacharya malik piris"
            },
            {
                "question": "ශ්‍රී ලංකාවේ සහ දකුණු ආසියානු කලාපයේ වෘක්ෂලතාදිය පිළිබඳ ඔහුගේ කටයුතු සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික උද්භිද විද්‍යාඥයා කවුද?",
                "a": "Dr. එස්ආර් කෝට්ටේගොඩ",
                "b": "Dr. සී.ජී.ඌරාගොඩ",
                "c": "Dr. පී.බී ප්‍රනාන්දු",
                "d": "Dr. ඒ.ආර්.පෙරේරා",
                "correct": "Dr. සී.ජී.ඌරාගොඩ",
                "speak": "acharya C P Uragoda"
            },
            {
                "question": "රාජකීය සංගමයේ සාමාජිකයෙකු ලෙස තේරී පත් වූ පළමු ශ්‍රී ලාංකිකයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. මලික් පීරිස්",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "ජල සම්පත් කළමනාකරණය සහ ජල විද්‍යාව සඳහා ඔහුගේ දායකත්වය සම්බන්ධයෙන් ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික ඉංජිනේරුවරයා කවුරුන්ද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මොහාන් මුණසිංහ",
                "c": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "d": "Prof. A.W.ජයවර්ධන",
                "correct": "Prof. A.W.ජයවර්ධන",
                "speak": "mahacharya A W Jayawardhena"
            },
            {
                "question": "අභ්‍යවකාශ විද්‍යාව සහ චන්ද්‍රිකා තාක්‍ෂණ ක්ෂේත්‍රයේ පුරෝගාමී ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "බෝවන රෝග පිළිබඳ වසංගතවේදය පිළිබඳ ඔහුගේ කාර්යය සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. මලික් පීරිස්",
                "b": "Prof. ROB විජේසේකර",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මලික් පීරිස්",
                "speak": "mahacharya malik piris"
            },
            {
                "question": "2021 භෞතික විද්‍යාව සඳහා නොබෙල් ත්‍යාගය පිරිනමන ශ්‍රී ලාංකික භෞතික විද්‍යාඥයා කවුද?",
                "a": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. ROB විජේසේකර",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "ශ්‍රී ලංකාවේ ජෛව විවිධත්වය පිළිබඳ පර්යේෂණ සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික ජීව විද්‍යාඥයා කවුද?",
                "a": "Dr. SR කෝට්ටේගොඩ",
                "b": "Dr. සී.ජී.ඌරාගොඩ",
                "c": "Dr. පී.බී ප්‍රනාන්දු",
                "d": "Dr. ඒ.ආර්.පෙරේරා",
                "correct": "Dr. SR කෝට්ටේගොඩ",
                "speak": "acharya SR kottogoda"
            },
            {
                "question": "කෘෂිකාර්මික විද්‍යා ක්ෂේත්‍රයේ කැපී පෙනෙන ශ්‍රී ලාංකික විද්‍යාඥයෙක් කවුද?",
                "a": "Dr. W.D.රත්නසූරිය",
                "b": "Dr. SR කෝට්ටේගොඩ",
                "c": "Dr. පී.බී ප්‍රනාන්දු",
                "d": "Dr. ඒ.ආර්.පෙරේරා",
                "correct": "Dr. W.D.රත්නසූරිය",
                "speak": "acharya W.D. Rathnasuriya"
            },
            {
                "question": "සමුද්‍ර ජීව විද්‍යාව අධ්‍යයනය සඳහා සැලකිය යුතු දායකත්වයක් ලබා දුන් ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Dr. එස්ආර් කෝට්ටේගොඩ",
                "b": "Dr. සී.ජී.ඌරාගොඩ",
                "c": "Dr. පී.බී ප්‍රනාන්දු",
                "d": "Dr. ඒ.ආර්.පෙරේරා",
                "correct": "Dr. ඒ.ආර්.පෙරේරා",
                "speak": "acharya A R perera"
            },
            {
                "question": "ස්වභාවික නිෂ්පාදන සහ ඖෂධ රසායන විද්‍යාව පිළිබඳ ඔහුගේ කාර්යය සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික රසායනඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. ROB විජේසේකර",
                "speak": "mahacharya R O B wijesinghe"
            },
            {
                "question": "දේශගුණික විපර්යාස සහ පාරිසරික විද්‍යාව පිළිබඳ ඔහුගේ කාර්යය සඳහා ප්‍රසිද්ධියට පත් ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මොහාන් මුණසිංහ",
                "speak": "mahacharya mohan munasinghe"
            },
            {
                "question": "ප්‍රතිශක්තිකරණ ක්ෂේත්‍රයේ ප්‍රමුඛ පෙළේ ශ්‍රී ලාංකික පර්යේෂකයෙක් කවුද?",
                "a": "Prof. මලික් පීරිස්",
                "b": "Prof. ROB විජේසේකර",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මලික් පීරිස්",
                "speak": "mahacharya malik piris"
            },
            {
                "question": "නැනෝ තාක්ෂණ ක්ෂේත්‍රයට සැලකිය යුතු දායකත්වයක් ලබා දී ඇති ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "ක්වොන්ටම් යාන්ත්‍ර විද්‍යාව පිළිබඳ පර්යේෂණ සඳහා ප්‍රසිද්ධ ශ්‍රී ලාංකික භෞතික විද්‍යාඥයා කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "speak": "mahacharya chandra wikramasinghe"
            },
            {
                "question": "ඝර්ම කලාපීය රෝග පිළිබඳ ඔහුගේ කාර්යය සඳහා ප්‍රසිද්ධියට පත් වූ ශ්‍රී ලාංකික විද්‍යාඥයා කවුද?",
                "a": "Prof. මලික් පීරිස්",
                "b": "Prof. ROB විජේසේකර",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මලික් පීරිස්",
                "speak": "mahacharya malik piris"
            },
            {
                "question": "ජාන විද්‍යා ක්ෂේත්‍රයේ කීර්තිමත් ශ්‍රී ලාංකික විද්‍යාඥයෙක් කවුද?",
                "a": "Prof. ROB විජේසේකර",
                "b": "Prof. මලික් පීරිස්",
                "c": "Prof. මොහාන් මුණසිංහ",
                "d": "Prof. චන්ද්‍රා වික්‍රමසිංහ",
                "correct": "Prof. මලික් පීරිස්",
                "speak": "mahacharya malik piris"
            }
        ]


# INITIAL SET questionArray
languageCheck()

# INITIATE MIXER
mixer.init()


# BACKGROUND SOUND PLAY
def playBackgroundMusic():
    mixer.music.load('images/kbc.mp3')
    mixer.music.play(-1)


# BACKGROUND SOUND PAUSE
def pauseBackgroundMusic():
    mixer.music.pause()


# INITIAL BACKGROUND SOUND PLAY
playBackgroundMusic()

# INITIATE TEXT TO SPEECH
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# START AGAIN GAME
def tryAgain(window):
    # DESTROY CHILD WINDOW
    window.destroy()

    # RESET VALUES
    selectedIds.clear()
    lifeLine50Button.config(image=image50, state=ACTIVE)
    lifeLineAudienceButton.config(image=imageAudiencePole, state=ACTIVE)
    lifeLineCallButton.config(image=imageCaller, state=ACTIVE)

    # SET LANGUAGE
    languageCheck()

    # SHOW AGAIN QUESTION
    addQuestion(questionId="", answer="")

    # BACKGROUND MUSIC
    playBackgroundMusic()


# CLOSE WINDOW IN LANGUAGE AND SOUND SETTINGS
def closeWindow(window):
    window.destroy()


# CHANGE LANGUAGE SETTING
def changeLanguage():
    # CHANGE GLOBAL lang VARIABLE
    def change(language):
        global lang
        lang = language
        # START GAME AGAIN
        tryAgain(languageWindow)

    # LANGUAGE WINDOW
    languageWindow = Toplevel()
    languageWindow.overrideredirect(True)
    languageWindow.config(bg="black", bd=0)
    languageWindow.geometry("500x220+100+100")

    # LANGUAGE WINDOW LABELS AND BUTTONS
    languageLabel = Label(languageWindow, text='Choose you language', background='black', activebackground="black",
                          foreground='white', activeforeground='white', font=('arial', 15, 'bold'))
    languageLabel.grid(row=0, column=0, pady=40)
    englishButton = Button(languageWindow, text='English', background='black', activebackground="black",
                           foreground='white', activeforeground='white', font=('arial', 15, 'bold'),
                           command=lambda: change("en"))
    englishButton.grid(row=1, column=0, pady=20)
    sinhalaButton = Button(languageWindow, text='සිංහල', background='black', activebackground="black",
                           foreground='white', activeforeground='white', font=('arial', 15, 'bold'),
                           command=lambda: change("sin"))
    sinhalaButton.grid(row=1, column=1, pady=20)
    closeButton = Button(languageWindow, image=closeImage, background='black', activebackground="black",
                         foreground='white',
                         activeforeground='white', font=('arial', 15, 'bold'),
                         command=lambda: closeWindow(languageWindow))
    closeButton.grid(row=1, column=2, pady=20, padx=60)


# BACKGROUND SETTING
def changeSound():
    # BACKGROUND SETTING WINDOW
    soundWindow = Toplevel()
    soundWindow.overrideredirect(True)
    soundWindow.config(bg="black", bd=0)
    soundWindow.geometry("500x220+100+100")

    # BACKGROUND SOUND WINDOW LABELS AND BUTTONS
    soundLabel = Label(soundWindow, text="Background music", background='black', activebackground="black",
                       foreground='white', activeforeground='white', font=('arial', 15, 'bold'))
    soundLabel.grid(row=0, column=0, pady=40)
    soundButton = Button(soundWindow, image=soundImage, background='black', activebackground="black",
                         foreground='white', activeforeground='white', font=('arial', 15, 'bold'),
                         command=playBackgroundMusic)
    soundButton.grid(row=1, column=0, pady=20)
    muteButton = Button(soundWindow, image=muteImage, background='black', activebackground="black", foreground='white',
                        activeforeground='white', font=('arial', 15, 'bold'), command=pauseBackgroundMusic)
    muteButton.grid(row=1, column=1, pady=20)
    closeButton = Button(soundWindow, image=closeImage, background='black', activebackground="black",
                         foreground='white',
                         activeforeground='white', font=('arial', 15, 'bold'), command=lambda: closeWindow(soundWindow))
    closeButton.grid(row=1, column=2, pady=20, padx=60)


# DEFINE WRONG ANSWER FOR LIFELINES 50 AND AUDIENCE POLE
def wrongAnswers(questionId):
    question = questionArray[questionId]
    wrongAnswersArray = []
    if question['a'] != question['correct']:
        wrongAnswersArray.append("a")
    if question['b'] != question['correct']:
        wrongAnswersArray.append("b")
    if question['c'] != question['correct']:
        wrongAnswersArray.append("c")
    if question['d'] != question['correct']:
        wrongAnswersArray.append("d")

    return wrongAnswersArray


# MAKE WRONG ANSWER EMPTY FOR LIFELINE 50
def optionMakeEmpty(changeId):
    if changeId == "a":
        optionOneButton.config(text="")
    if changeId == "b":
        optionTwoButton.config(text="")
    if changeId == "c":
        optionThreeButton.config(text="")
    if changeId == "d":
        optionFourButton.config(text="")


# LIFELINE 50
def lifeLine50(questionId):
    # GET WRONG ANSWERS ARRAY
    wrongAnswersArray = wrongAnswers(questionId)

    # GET RANDOMLY 2 WRONG ANSWERS FOR EMPTY
    changingId1 = randint(0, 2)
    changingId2 = None
    isChanginNotIdsSelected = True
    while isChanginNotIdsSelected:
        changingId2 = randint(0, 2)
        if changingId1 != changingId2:
            isChanginNotIdsSelected = False

    # REMOVE WRONG 2 ANSWERS
    optionMakeEmpty(wrongAnswersArray[changingId1])
    optionMakeEmpty(wrongAnswersArray[changingId2])
    # CHANGE IMAGE AND STATE
    lifeLine50Button.config(image=image50X, state=DISABLED)


# LIFELINE AUDIENCE POLE
def lifeLineAudience(questionId):
    # GET WRONG ANSWERS ARRAY
    wrongAnswersArray = wrongAnswers(questionId)

    # GET PROGRESS BAR VALUES RANDOMLY
    if 'a' in wrongAnswersArray:
        valueA = randint(0, 60)
    else:
        valueA = randint(60, 85)
    if 'b' in wrongAnswersArray:
        valueB = randint(0, 60)
    else:
        valueB = randint(60, 85)
    if 'c' in wrongAnswersArray:
        valueC = randint(0, 60)
    else:
        valueC = randint(60, 85)
    if 'd' in wrongAnswersArray:
        valueD = randint(0, 60)
    else:
        valueD = randint(60, 85)

    # SET PROGRESS BAR
    progressBarA.config(value=valueA)
    progressBarB.config(value=valueB)
    progressBarC.config(value=valueC)
    progressBarD.config(value=valueD)

    # PLACE PROGRESS BARS
    progressBarA.place(x=420, y=170)
    progressBarB.place(x=460, y=170)
    progressBarC.place(x=500, y=170)
    progressBarD.place(x=540, y=170)
    progressBarALabel.place(x=423, y=270)
    progressBarBLabel.place(x=463, y=270)
    progressBarCLabel.place(x=503, y=270)
    progressBarDLabel.place(x=543, y=270)
    # CHANGE IMAGE AND STATE
    lifeLineAudienceButton.config(image=imageAudiencePoleX, state=DISABLED)


# LIFELINE CALL A FRIEND
def lifeLineCall(questionId):
    phoneLabel.place(x=80, y=190)
    # CHANGE BUTTON IMAGE AND STATE
    lifeLineCallButton.config(image=imageCallerX, state=DISABLED)
    # PLAY RINGING MUSIC
    mixer.music.load('images/calling.mp3')
    mixer.music.play(loops=2)
    # WAIT TILL PLAY RINGING MUSIC
    time.sleep(8)
    # GET SPEAK FROM THE QUESTION ARRAY
    answer = questionArray[questionId]['speak']
    # TEXT SPEECH
    engine.say(f'The answer is {answer}')
    engine.say(f'The answer is {answer}')
    engine.runAndWait()


# QUESTION
def addQuestion(questionId, answer):
    # HIDE PROGRESS BARS AND LABELS
    progressBarA.place_forget()
    progressBarB.place_forget()
    progressBarC.place_forget()
    progressBarD.place_forget()
    progressBarALabel.place_forget()
    progressBarBLabel.place_forget()
    progressBarCLabel.place_forget()
    progressBarDLabel.place_forget()
    # HIDE PHONE LABEL
    phoneLabel.place_forget()

    # WON
    def won():
        # WON WINDOW
        wonWindow = Toplevel()
        wonWindow.overrideredirect(True)
        wonWindow.config(bg="black", bd=0)
        wonWindow.geometry("500x400+100+100")
        imgLabel = Label(wonWindow, image=imageMiddle, bg="black")
        imgLabel.pack(pady=30)

        # LABELS AND BUTTONS
        correctAnswerLabel = Label(wonWindow, text="Congratulations", font=('arial', 14, 'bold'), background='black',
                                   foreground='yellow')
        correctAnswerLabel.pack()
        loseLabel = Label(wonWindow, text="You Won.", font=('arial', 20, 'bold'), background='black',
                          foreground='white')
        loseLabel.place(x=180, y=270)
        tryAgainButton = Button(wonWindow, font=('arial', 15, 'bold'), text='Try Again', background="black", bd=0,
                                foreground="white",
                                activebackground='black', activeforeground='white',
                                command=lambda: tryAgain(wonWindow))
        tryAgainButton.place(x=190, y=300)
        exitButton = Button(wonWindow, font=('arial', 15, 'bold'), text='Exit', background="black", bd=0,
                            foreground="white",
                            activebackground='black', activeforeground='white', command=lambda: exit(wonWindow))
        exitButton.place(x=215, y=330)
        happyLabel = Label(wonWindow, image=happyImage, bg='black', bd=0)
        happyLabel.place(x=60, y=280)
        happyLabel1 = Label(wonWindow, image=happyImage, bg='black', bd=0)
        happyLabel1.place(x=360, y=280)

        # PLAY WON MUSIC
        mixer.music.load('images/Kbcwon.mp3')
        mixer.music.play()

    def showQuestion():
        # FIND NOT SHOWED ID FROM QUESTION ARRAY RANDOMLY
        isNotAdded = True
        while isNotAdded:
            idValue = randint(0, len(questionArray) - 1)
            if idValue not in selectedIds:
                selectedIds.append(idValue)
                isNotAdded = False

        # RESET QUESTION AREA
        questionArea.delete(1.0, END)
        questionArea.insert(END, questionArray[idValue]['question'])
        # LABELS AND BUTTONS
        optionOneButton.config(text=questionArray[idValue]['a'],
                               command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['a']))
        optionTwoButton.config(text=questionArray[idValue]['b'],
                               command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['b']))
        optionThreeButton.config(text=questionArray[idValue]['c'],
                                 command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['c']))
        optionFourButton.config(text=questionArray[idValue]['d'],
                                command=lambda: addQuestion(questionId=idValue, answer=questionArray[idValue]['d']))
        amountLabel.config(image=amountImageArray[len(selectedIds) - 1])
        lifeLine50Button.config(command=lambda: lifeLine50(questionId=idValue))
        lifeLineAudienceButton.config(command=lambda: lifeLineAudience(questionId=idValue))
        lifeLineCallButton.config(command=lambda: lifeLineCall(questionId=idValue))

    # CLOSE PROGRAM
    def exit(widow):
        widow.destroy()
        root.destroy()

    # GAME FAIL
    def fail(questionId):
        # WINDOW
        failWindow = Toplevel()
        failWindow.overrideredirect(True)
        failWindow.config(bg="black", bd=0)
        failWindow.geometry("500x400+100+100")
        imgLabel = Label(failWindow, image=imageMiddle, bg="black")
        imgLabel.pack(pady=30)

        # GET CORRECT ANSWER FROM QUESTION ARRAY
        correctAnswer = questionArray[questionId]['correct']

        # LABELS AND BUTTONS
        correctAnswerLabel = Label(failWindow, text=correctAnswer, font=('arial', 14, 'bold'), background='black',
                                   foreground='yellow')
        correctAnswerLabel.pack()
        loseLabel = Label(failWindow, text="You Lose.", font=('arial', 20, 'bold'), background='black',
                          foreground='white')
        loseLabel.place(x=180, y=270)
        tryAgainButton = Button(failWindow, font=('arial', 15, 'bold'), text='Try Again', background="black", bd=0,
                                foreground="white",
                                activebackground='black', activeforeground='white',
                                command=lambda: tryAgain(failWindow))
        tryAgainButton.place(x=190, y=300)
        exitButton = Button(failWindow, font=('arial', 15, 'bold'), text='Exit', background="black", bd=0,
                            foreground="white",
                            activebackground='black', activeforeground='white', command=lambda: exit(failWindow))
        exitButton.place(x=215, y=330)
        sadLabel = Label(failWindow, image=sadImage, bg='black', bd=0)
        sadLabel.place(x=60, y=280)
        sadLabel1 = Label(failWindow, image=sadImage, bg='black', bd=0)
        sadLabel1.place(x=360, y=280)

    if questionId == "":
        # FIRST QUESTION
        showQuestion()
    else:
        if questionArray[questionId]['correct'] == answer:
            if len(selectedIds) != 16:
                showQuestion()
            else:
                won()
        else:
            fail(questionId)


# UI============================================
# MAIN WINDOW
root = Tk()
root.geometry("1000x630+0+0")
root.resizable(False, False)
root.title("Who wants to be a millionaire")
root.config(background="black")

# LEFT FRAME
leftFrame = Frame(root, bg='black')
leftFrame.grid(row=0, column=0)

# TOP LEFT FRAME
topLeftFrame = Frame(leftFrame, padx=10, bg="black")
topLeftFrame.grid(row=0, column=0)

# MIDDLE LEFT FRAME
middleLeftFrame = Frame(leftFrame, bg="black")
middleLeftFrame.grid(row=1, column=0)

# BOTTOM LEFT FRAME
bottomLeftFrame = Frame(leftFrame, bg="black")
bottomLeftFrame.grid(row=2, column=0)

# LANGUAGE SETTING BUTTON
languageButton = Button(topLeftFrame, text="Change Language", background="black", foreground="white",
                        activebackground="black", activeforeground="white", command=changeLanguage)
languageButton.grid(row=0, column=0)

# BACKGROUND SOUND BUTTON
backgroundSoundButton = Button(topLeftFrame, text="Music", background="black", foreground="white",
                               activebackground="black", activeforeground="white", command=changeSound)
backgroundSoundButton.grid(row=0, column=1)

# LIFELINE 50
image50 = PhotoImage(file="images/50-50.png")
image50X = PhotoImage(file="images/50-50-X.png")

lifeLine50Button = Button(topLeftFrame, image=image50, background="black", bd=0, activebackground="black", width=170,
                          height=75)
lifeLine50Button.grid(row=1, column=0)

# LIFELINE AUDIENCE POLE
imageAudiencePole = PhotoImage(file="images/audiencePole.png")
imageAudiencePoleX = PhotoImage(file="images/audiencePoleX.png")

lifeLineAudienceButton = Button(topLeftFrame, image=imageAudiencePole, background="black", bd=0,
                                activebackground="black", width=170, height=75)
lifeLineAudienceButton.grid(row=1, column=1)

# LIFELINE CALLER FRIEND
imageCaller = PhotoImage(file="images/phoneAFriend.png")
imageCallerX = PhotoImage(file="images/phoneAFriendX.png")
imagePhone = PhotoImage(file="images/phone.png")

lifeLineCallButton = Button(topLeftFrame, image=imageCaller, background="black", bd=0, activebackground="black",
                            width=170, height=75)
lifeLineCallButton.grid(row=1, column=2)

# CALL A FRIEND PHONE LABEL
phoneLabel = Label(root, image=imagePhone, bg='black')

imageMiddle = PhotoImage(file="images/center.png")

# MIDDLE IMAGE LABEL
middleLabel = Label(middleLeftFrame, image=imageMiddle, bg="black", height=250)
middleLabel.grid(row=0, column=0)

# QUESTION AREA
imageLayout = PhotoImage(file="images/lay.png")

layoutLabel = Label(bottomLeftFrame, image=imageLayout, bg="black")
layoutLabel.grid(row=0, column=0)

# QUESTION
questionArea = Text(bottomLeftFrame, font=('arial', 13, 'bold'), bg='black', fg='white', width=35, height=3,
                    wrap='word', bd=0)
questionArea.place(x=70, y=10)

# ANSWERS
# A================
aLabel = Label(bottomLeftFrame, text="A: ", bg="black", font=('arial', 11, 'bold'), fg="white")
aLabel.place(x=40, y=110)
optionOneButton = Button(bottomLeftFrame, bg="black", font=('arial', 11, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionOneButton.place(x=60, y=107)

# B================
bLabel = Label(bottomLeftFrame, text="B: ", bg="black", font=('arial', 11, 'bold'), fg="white")
bLabel.place(x=315, y=110)
optionTwoButton = Button(bottomLeftFrame, bg="black", font=('arial', 11, 'bold'), fg="white", bd=0,
                         activebackground='black', activeforeground='white', cursor='hand2')
optionTwoButton.place(x=335, y=107)

# C================
cLabel = Label(bottomLeftFrame, text="C: ", bg="black", font=('arial', 11, 'bold'), fg="white")
cLabel.place(x=40, y=190)
optionThreeButton = Button(bottomLeftFrame, bg="black", font=('arial', 11, 'bold'), fg="white",
                           bd=0,
                           activebackground='black', activeforeground='white', cursor='hand2')
optionThreeButton.place(x=60, y=187)

# D================
dLabel = Label(bottomLeftFrame, text="D: ", bg="black", font=('arial', 11, 'bold'), fg="white")
dLabel.place(x=315, y=190)
optionFourButton = Button(bottomLeftFrame, bg="black", font=('arial', 11, 'bold'), fg="white", bd=0,
                          activebackground='black', activeforeground='white', cursor='hand2')
optionFourButton.place(x=335, y=187)

# PROGRESS BAR
progressBarA = Progressbar(root, orient=VERTICAL)
progressBarB = Progressbar(root, orient=VERTICAL)
progressBarC = Progressbar(root, orient=VERTICAL)
progressBarD = Progressbar(root, orient=VERTICAL)

progressBarALabel = Label(root, text='A', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarBLabel = Label(root, text='B', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarCLabel = Label(root, text='C', bg="black", foreground="white", font=('arian', 15, 'bold'))
progressBarDLabel = Label(root, text='D', bg="black", foreground="white", font=('arian', 15, 'bold'))

# RIGHT FRAME
rightFrame = Frame(root)
rightFrame.grid(row=0, column=1)

# RIGHT FRAME IMAGES
amountImage0 = PhotoImage(file="images/Picture0.png")
amountImage1 = PhotoImage(file="images/Picture1.png")
amountImage2 = PhotoImage(file="images/Picture2.png")
amountImage3 = PhotoImage(file="images/Picture3.png")
amountImage4 = PhotoImage(file="images/Picture4.png")
amountImage5 = PhotoImage(file="images/Picture5.png")
amountImage6 = PhotoImage(file="images/Picture6.png")
amountImage7 = PhotoImage(file="images/Picture7.png")
amountImage8 = PhotoImage(file="images/Picture8.png")
amountImage9 = PhotoImage(file="images/Picture9.png")
amountImage10 = PhotoImage(file="images/Picture10.png")
amountImage11 = PhotoImage(file="images/Picture11.png")
amountImage12 = PhotoImage(file="images/Picture12.png")
amountImage13 = PhotoImage(file="images/Picture13.png")
amountImage14 = PhotoImage(file="images/Picture14.png")
amountImage15 = PhotoImage(file="images/Picture15.png")

# LEFT FRAME IMAGES MAKE AS ARRAY
amountImageArray = [
    amountImage0,
    amountImage1,
    amountImage2,
    amountImage3,
    amountImage4,
    amountImage5,
    amountImage6,
    amountImage7,
    amountImage8,
    amountImage9,
    amountImage10,
    amountImage11,
    amountImage12,
    amountImage13,
    amountImage14,
    amountImage15
]

# RIGHT FRAME IMAGE LABEL
amountLabel = Label(rightFrame, bg="black")
amountLabel.grid(row=0, column=0)

# SAD AND HAPPY IMAGES
happyImage = PhotoImage(file="images/happy.png")
sadImage = PhotoImage(file="images/sad.png")

# ADD FIRST QUESTION
addQuestion(questionId="", answer="")

# SOUND OPTION IMAGE
soundImage = PhotoImage(file='images/sound.png')
muteImage = PhotoImage(file='images/mute.png')
closeImage = PhotoImage(file='images/close.png')

# LOOP MAIN FRAME
root.mainloop()
