# This is the Stable Matching Gale Shapley Algorithm 
# Gale Shapley describes the method of Stable One to One matching
# According to it A man can be engaged to a woman based on their Preferences


def init_free_men():
    for man in prefered_ranking_men:
        free_men.append(man)

def stable_match():
    while len(free_men) > 0:
        for man in free_men:
            start_matching(man)

def start_matching(man):
    for woman in prefered_ranking_men[man]:
        taken_match = [couple for couple in temporary_engagement if woman in couple]
        
        if len(taken_match) == 0:
            temporary_engagement.append([man, woman])
            free_men.remove(man)
            break

        elif len(taken_match) > 0:
            current_guy = prefered_ranking_women[woman].index(taken_match[0][0])
            potential_guy = prefered_ranking_women[woman].index(man)

            if current_guy >= potential_guy:
                free_men.remove(man)
                free_men.append(taken_match[0][0])
                taken_match[0][0] = man
                break

            

prefered_ranking_men = {
    'Alice': ['Frank', 'Eva', 'Dave'],
    'Bob': ['Frank', 'Dave', 'Eva'],
    'Carol': ['Dave', 'Eva', 'Frank']
}

prefered_ranking_women = {
    'Dave': ['Carol', 'Alice', 'Bob'],
    'Eva': ['Alice', 'Bob', 'Carol'],
    'Frank': ['Carol', 'Alice', 'Bob']
}

# This will store all the paired men and women 
# until the loop ends
# This list will store the current engagements in the format [man, woman]
temporary_engagement = []

# This will store all the men who are yet 
# to be paired and are still single
# Initially, all the men are considered free and added to this list.
free_men = []


init_free_men()
stable_match()
print("Final Matching:", temporary_engagement)
