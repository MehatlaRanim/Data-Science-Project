# NLP-Project
The system comprises several interconnected classes:
TextPreprocessor() , PositionalInvertedIndex() , Query() , BooleanSearch(),
PhraseSearch(), TFIDF().

**1-Tokenization and Stemming**
The TextPreprocessor() class focuses on text preprocessing (removing stop words ,
tokenization and stemming) .
Tokenization breaks text into tokens, typically words or sentences. we utilized the
Natural Language Toolkit (nltk) library for tokenization, employing methods like word
tokenization using word_tokenize() .
Stemming, the process of reducing words to their base or root form, was accomplished
using the Porter Stemmer algorithm available in nltk. This step standardizes words to
their base form, allowing for better matching during search operations.

**2-Inverted Index Implementation**
The PositionalInvertedIndex() class serves as the backbone of the system,
constructing an inverted index for the corpus. The index is a mapping of terms to the
documents in which they appear, along with additional information such as term
frequency and positional information.

**3-Search Function Implementations**
Boolean Search
The BooleanSearch() class enables users to perform Boolean operations (AND, OR,
NOT) on the inverted index. It processes user queries and retrieves relevant documents
based on the Boolean logic applied to the index. This functionality is critical for basic
information retrieval operations.
Phrase Search
The PhraseSearch() class handles more complex queries by considering the positions
of terms in documents. It allows users to search for sequences of words or phrases
within documents. This is achieved by utilizing the positional information stored in the
inverted index.

**4-TF-IDF Calculation**
The TFIDF() class calculates the TF-IDF (Term Frequency-Inverse Document
Frequency) scores for terms in the corpus. This scoring system evaluates the importance
of a term in a document relative to its frequency in the entire corpus. TF-IDF scores aid
in ranking and retrieving documents based on relevance to user queries.

** Web Scraping**
Web scraping is a powerful technique employed to gather data from websites, allowing
for the extraction of valuable information for various purposes. In our project, we aimed
to analyze the Israel-Palestine conflict by collecting data from different sources,
including news articles and tweets.
