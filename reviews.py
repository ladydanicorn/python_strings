#Assignment 1

#Task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    modified_review = review
    
    for keyword in keywords:
        if keyword in modified_review.lower():  
            modified_review = modified_review.replace(keyword, keyword.upper())
    
    print(modified_review)

#Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    
    for review in reviews:
        review_lower = review.lower()

        for word in positive_words:
            if word in review_lower:
                positive_count += 1
        
        for word in negative_words:
            if word in review_lower:
                negative_count += 1

    return positive_count, negative_count

pos_count, neg_count = sentiment_tally(reviews, positive_words, negative_words)

print(f"Positive words: {pos_count}")
print(f"Negative words: {neg_count}")

#Task 3

def review_summary(review):
    if len(review) <= 30:
        return review + "..."
    
    summary = review[:30]

    last_space = summary.rfind(' ')

    if last_space != -1:
        summary = summary[:last_space]

    summary += "..."

    return summary

for review in reviews:
    print(review_summary(review))