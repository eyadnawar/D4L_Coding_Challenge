import psycopg2
import psycopg2.extras
import time

def token_reader_sorted_tokens():
    conn = psycopg2.connect(dbname= 'postgres', user= 'postgres', password= 'select33')
    cur = conn.cursor()
    cur.execute("CREATE TABLE tokens (token VARCHAR);")
    conn.commit()

    start_time = time.time()

    file = open('C:/Users/Lenovo/Desktop/D4L.txt', 'r')
    lister = file.readlines()
    lister.sort()
    file.close()
    my_dict = dict()
    final_list = []
    final_list.append(lister[0][0:-1])

    for i in range(1, len(lister)):
        if(lister[i] != lister[i-1]):
            final_list.append(lister[i][0:-1])
        else:
            word = lister[i][0:-1]
            if(word in my_dict):
                my_dict[word] = my_dict.get(word) + 1
            else:
                my_dict[word] = 1

    lister.clear()
    data = [(word,) for word in final_list]
    insert_query = 'insert into tokens (token) values %s'
    psycopg2.extras.execute_values (cur, insert_query, data)
    conn.commit()

    print("--- %s seconds ---" % (time.time() - start_time))
    print("length of dictionary = ", len(my_dict))
    print(my_dict)

    cur.close()
    conn.close()
    return