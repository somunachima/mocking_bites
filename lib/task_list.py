class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def all(self):
        return self.tasks

    def all_complete(self):
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])

# def test_diary_counts_words_in_all_entries_with_mocks():
#     diary = Diary()

#     fake_two_word_diary_entry = Mock()
#     fake_two_word_diary_entry.count_words.return_value = 2

#     fake_three_word_diary_entry = Mock()
#     fake_three_word_diary_entry.count_words.return_value = 3

#     diary.add(fake_two_word_diary_entry)
#     diary.add(fake_three_word_diary_entry)

#     assert diary.count_words() == 5
