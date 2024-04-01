# finalCapstone
Sentiment Analysis Report
Run He/RH23110011704

1.Introduction:

This sentiment analysis report aims to analyze the sentiment of customer reviews using natural language processing (NLP) techniques. The provided code utilizes the TextBlob library to perform sentiment analysis on a dataset of Amazon product reviews. This report discusses the logic behind the code, the process followed, and evaluates its benefits and deficiencies.

2.Data Overview:
Total Reviews Analyzed: 5000

3.Sentiment Analysis Methodology:
- **Preprocessing**: The code begins by preprocessing the text data, including removing stopwords and converting text to lowercase to enhance the accuracy of sentiment analysis.
- **Sentiment Analysis**: Sentiment analysis is performed using TextBlob's `sentiment.polarity` attribute, which calculates the polarity of each review text.
- **Classification**: Reviews are classified into three categories based on polarity scores: Positive, Neutral, and Negative.
- **Accuracy Evaluation**: The accuracy of the sentiment analysis is evaluated by comparing predicted sentiments with actual review scores.

Reviews were classified into three categories:
Positive: Sentiment polarity > 0.3
Neutral: Sentiment polarity = 0.3
Negative: Sentiment polarity < 0.3

4.Results:
Positive Reviews: 4374
Neutral Reviews: 401
Negative Reviews: 225

5.Accuracy Evaluation:
The accuracy of the sentiment analysis was evaluated by comparing the predicted sentiment with the actual review scores.
The final accuracy of the sentiment analysis is around: 0.85

6. Analysis Results:
Based on the sentiment analysis results, it can be observed that the majority of reviews are positive.
Further analysis or action may be required to address the negative reviews and improve overall customer satisfaction.


7.Benefits:

- Automated Analysis: The code automates the sentiment analysis process, enabling quick and efficient analysis of large datasets.
- Data-driven Decisions: Insights from sentiment analysis can inform data-driven decisions, such as product improvements or marketing strategies.
- Scalability: The code can be applied to diverse datasets and customized for various applications.

8.Deficiencies:

- **Sensitivity to Language**: The sentiment analysis accuracy may vary based on language nuances and context, potentially leading to misinterpretations.
- **Threshold Sensitivity**: The choice of sentiment polarity threshold (e.g., 0.3) may affect the classification accuracy and requires careful selection.
- **Limited Contextual Understanding**: TextBlob's sentiment analysis may lack contextual understanding, leading to oversimplified classifications.

6. Conclusion:

While the sentiment analysis code provides valuable insights into customer sentiments, it is essential to interpret the results cautiously, considering its limitations. Further enhancements, such as incorporating domain-specific sentiment lexicons or leveraging advanced machine learning models, could improve the accuracy and contextual understanding of sentiment analysis.

