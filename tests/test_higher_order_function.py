# sample
# def display_log_title(title, formatter_func):
#     print(formatter_func(title))
#
#
# def format_to_upper(title: str):
#     return title.upper()
#
#
# def format_with_double_sharps(title: str):
#     return f"## {title} ##"
#

# Execution
# display_log_title("Black Pink", format_to_upper)
# display_log_title("Black Pink", format_with_double_sharps)


# Sample 2
# logs = [
#     {"title": "walk", "mood": "happy", "task": "exercise"},
#     {"title": "meeting", "mood": "tired", "task": "work"},
#     {"title": "coding", "mood": "focused", "task": "study"}
# ]
#
#
# def summarize_logs(data, strategy_func):
#     return strategy_func(data)
#
#
# def summarize_titles(data: [dict]):
#     return ','.join([d['title'] for d in data])
#

# This method works but too many loops
## def summarize_moods(data: [dict]):
##     mood = [d['mood'] for d in data]
##     return {m: mood.count(m) for m in mood}

#
# def summarize_moods(data: [dict]):
#     mood_count = {}
#     for entry in data:
#         mood = entry['mood']
#         mood_count[mood] = mood_count.get(mood, 0) + 1
#     return mood_count
#

# print(summarize_logs(logs, summarize_titles))
# print(summarize_logs(logs, summarize_moods))


# sample 3

logs = [
    {"title": "walk", "mood": "happy", "task": "exercise"},
    {"title": "meeting", "mood": "tired", "task": "work"},
    {"title": "coding", "mood": "focused", "task": "study"},
    {"title": "gym", "mood": "happy", "task": "exercise"}
]

#
# def summarize_logs(data, filter_func, summary_func):
#     filtered = filter_func(data)
#     return summary_func(filtered)
#
#
# def filter_exercise(data):
#     return [d for d in data if d['task'] == 'exercise']
#
#
# def filter_all(data):
#     return data  # no filter
#
#
# def summarize_titles(data):
#     return ', '.join([d['title'] for d in data])
#
#
# def summarize_moods(data):
#     mood_counts = {}
#     for d in data:
#         mood = d['mood']
#         mood_counts[mood] = mood_counts.get(mood, 0) + 1
#     return mood_counts
#
#
# # Try with different filters and summaries:
# print(summarize_logs(logs, filter_exercise, summarize_titles))
# print(summarize_logs(logs, filter_all, summarize_moods))

#
# def summarize_log(data, filter_func, summarize_func):
#     filtered = filter_func(data)
#     return summarize_func(filtered)
#
#
# def filter_exercise(data) -> list:
#     return [d for d in data if d['task'] == 'exercise']
#
#
# def filter_happy(data) -> list:
#     return [d for d in data if d['mood'] == 'happy']
#
#
# def filter_all(data) -> list:
#     return data
#
#
# def summarize_title(data) -> str:
#     return ','.join([d['title'] for d in data])
#
#
# def summarize_mood(data) -> dict:
#     count_mood = {}
#     for d in data:
#         key = d['mood']
#         count_mood[key] = count_mood.get(key, 0) + 1
#     return count_mood
#
#
# print(summarize_log(logs, filter_happy, summarize_title))
# print(summarize_log(logs, filter_exercise, summarize_mood))


from functools import partial


def filter_by_mood(data, mood):
    return [d for d in data if d['mood'] == mood]


def summarize_task_counts(data):
    count_task = {}
    for entry in data:
        key = entry['task']
        count_task[key] = count_task.get(key, 0) + 1
    return count_task


happy_data = partial(filter_by_mood, mood='happy')

print(summarize_task_counts(happy_data(logs)))
# print(summarize_task_counts(filter_by_mood(logs, 'happy')))


def filter_by_task(data, task):
    return [entry for entry in data if entry['task'] == task]


exercise_data = partial(filter_by_task, task='exercise')

filtered = exercise_data(happy_data(logs))
print(filtered)

filtered_reversed = happy_data(exercise_data(logs))
print(filtered_reversed)

