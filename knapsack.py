def get_matrix(wt, val, W):
    no_items = len(wt)
    knap_mat = [[0 for i in range(W+1)] for j in range(no_items)]
    for i in range(no_items):
        for j in range(W+1):
            if(j < wt[i]):
                try:
                    knap_mat[i][j] = knap_mat[i-1][j]
                except IndexError:
                    knap_mat[i][j] = 0
            else:
                knap_mat[i][j] = max(knap_mat[i-1][j], val[i] + knap_mat[i-1][j-wt[i]])
    return [[0 for i in range(W+1)]] + knap_mat


def back_track(knap_mat, W, wt, val):
    item = len(wt)
    weight = W
    items = []
    while(item != 0):
        if(knap_mat[item][weight] != knap_mat[item-1][weight]):
            weight -= wt[item-1]
            items.append(item-1)
        item -= 1    
    return items



wt =[1,3,4,5] 
val =  [1,4,5,7]
W = 20

knap_mat = get_matrix(wt, val, W)
for i in range(len(knap_mat)):
    print(knap_mat[i])

items = back_track(knap_mat, W, wt, val)
print(items)
print([wt[i] for i in items])
