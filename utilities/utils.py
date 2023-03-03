
class Utils:
    def get_filtered_results(self, list):
        for items in list:
            print(items.text)

def assertInListItem(self, list, textassert):
    for alltitles in list:
        if textassert in alltitles:
            print("Titles that have"+ textassert +"in list",alltitles.text)