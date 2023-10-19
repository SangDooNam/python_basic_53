"""Task 1"""



users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]

# def get_item(name_author, hit_list=[]):
    
#     for author in users:
#         if name_author == author['name']:
#             for lst in author['items']:
#                 if 'reads' in lst:
#                     hit_list.append(lst['reads'])
                
#                     return hit_list


# def has_hits(name_author):
    
#     if not get_item(name_author) or all(number < 1000 for number in get_item(name_author)):
#         return False
#     elif any(number > 1000 for number in get_item(name_author)):
#         return True


# print("Clark", has_hits("Clark"))
# print("Peter", has_hits("Peter"))
# print("Samantha", has_hits("Samantha"))
# print("Mathilda", has_hits("Mathilda"))
# print("Mario", has_hits("Mario"))

"""Task 2"""


# def get_item(name_author):
    
#     for author in users:
#         hit_list=[]
#         if name_author == author['name']:
#             for lst in author['items']:
#                 if 'reads' in lst and lst['status'] == 'Published':
#                     hit_list.append(lst['reads'])
                
#             return hit_list

# def author_average_reads(name_author):
    
#     if not get_item(name_author):
#         return 0
#     else:
#         return int(sum(get_item(name_author)) / len(get_item(name_author)))


# print("Clark", author_average_reads("Clark"))
# print("Peter", author_average_reads("Peter"))
# print("Samantha", author_average_reads("Samantha"))
# print("Mathilda", author_average_reads("Mathilda"))
# print("Mario", author_average_reads("Mario"))


"""Task 3"""


def clark():
    
    if users[0]['items'][0]['status'] == 'Published':
        return (users[0]['items'][0]['reads']) / 1 > 1000
    return False


def peter():
    
    for item in users[1]['items']:
        if 'status' in users[1]['items'] and users[1]['items']['status'] == 'Published':
            return (item.get('reads') / 1 ) > 1000
    return False

def samantha():
    if users[2]['items'][0]['status'] == "Published" and users[2]['items'][1]['status']:
        return (users[2]['items'][0]['reads'] + users[2]['items'][1]['reads']) / 2 > 1000
    return False


def mathilda():
    
    for item in users[3]['items']:
        if 'status' in users[3]['items'] and users[1]['items']['status'] == 'Published':
            return (item.get('reads') / 1) < 1000
    return False

def author_is_popular(name_author):
    
    while name_author == 'Clark':
        return clark()
    while name_author == 'Peter':
        return peter()
    while name_author == 'Samantha':
        return samantha()
    while name_author == 'Mathilda':
        return mathilda()
    while name_author == 'Mario':
        return False
    

print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))


