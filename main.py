""""
    Computing Ratings
    news_ratings: [1, 10]
    user_scores: [0, 1.0]
    fake_news: 1
    conspiracy: 3
    suspesions: 5
    valid: 10
"""


def compute_news_rating(news, reviewers, scores_recieved, reviewers_rating):
    # TODO: retrieve list of reviewers that reviewed this news
    news_scores = 0
    for idx in range(len(reviewers)):
        news_scores += reviewers_rating[idx] * scores_recieved[idx]

    total_scores = sum(reviewers_rating)
    news_rating = round(news_scores/total_scores, 2)
    print('News Article with title "{0}" has rating of {1}'.format(news, news_rating))

    # TODO: add news score for article and save it in db

    # TODO: re-calculate user reviewers score according to news score save it in db

    return


def compute_user_rating_at_beginning(name, discount_factor_experience, gt_review_scores, user_review_items_scores):
    user_total_item_reviews = len(user_review_items_scores)

    diff_scores = 0
    for idx in range(user_total_item_reviews):
        diff_scores += abs(gt_review_scores[idx] - user_review_items_scores[idx])
    user_rating = round(discount_factor_experience * (1 - (diff_scores/sum(gt_review_scores))), 2)
    print('{0} has rating of {1}'.format(name, user_rating))
    return


def compute_user_rating_iterative(user_new_review, item_current_score, total_user_items_scores, total_item_scores):
    # discount user experience
    discounting_user_factor = 1 - 1/total_user_items_scores

    # discount number of reviews for item
    discounting_item_factor = 1 - 1/total_item_scores

    diff_score = abs(user_new_review - item_current_score)
    user_new_rating = discounting_user_factor * (1 - (discounting_item_factor * diff_score/item_current_score))
    print('News user rating is {0}'.format(user_new_rating))
    return
    # TODO: update user new rating


def example_compute_news_rating():
    news = "EU is fighting against corona virus"
    # computing news "corona" article
    reviewers = {'laura': 0, "lena": 1, "tim": 2}
    scores_recieved = {"laura": 6, "lena": 10, "tim": 10}
    reviewers_rating = {"laura": 0.8, "lena": 0.6, "tim": 1}

    compute_news_rating(news, list(reviewers.values()), list(scores_recieved.values()), list(reviewers_rating.values()))


def example_compute_user_rating_at_beginning():
    user_name = 'Alan Turing'
    discount_factor_experience = 0.1
    gt_review_scores = {'article1': 1, "article2": 5, "article3": 10}
    user_review_items_scores = {'article1': 1, "article2": 10, "article3": 10}

    compute_user_rating_at_beginning(user_name, discount_factor_experience,
                                     list(gt_review_scores.values()), list(user_review_items_scores.values()))


def example_compute_user_rating_iterative():
    # updating user score
    total_user_reviews_cnt = 5
    user_new_review = 7
    total_item_review_cnt = 4
    item_current_score = 6.2

    compute_user_rating_iterative(user_new_review, item_current_score, total_user_reviews_cnt, total_item_review_cnt)


if __name__ == '__main__':
    #example_compute_news_rating()
    # example_compute_user_rating_at_beginning()
    example_compute_user_rating_iterative()