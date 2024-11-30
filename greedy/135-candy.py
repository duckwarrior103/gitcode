class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return 1
        answers = [1] * len(ratings)
        for i, rating in enumerate(ratings):
            if i == len(ratings)-1 and ratings[i-1] < rating or i > 0 and  ratings[i-1] < rating <= ratings[i+1]:
                answers[i] = answers[i-1] + 1
        for i in range(len(ratings)-1, -1, -1):
            if i == 0 and ratings[i] > ratings[i+1] or i < len(ratings) - 1 and ratings[i+1] < ratings[i] <= ratings[i-1]:
                answers[i] = answers[i+1] + 1
        for i, rating in enumerate(ratings):
            if i > 0 and i < len(ratings) - 1 and ratings[i-1] < rating > ratings[i+1]:
                answers[i] = max(answers[i-1], answers[i+1]) + 1
        return sum(answers)

