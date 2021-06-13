import psycopg2
import psycopg2.extras
import time

def token_reader_hashset(file_path):
    conn = psycopg2.connect(dbname= 'postgres', user= 'postgres', password= 'select33')
    cur = conn.cursor()
    cur.execute("CREATE TABLE tokens (token VARCHAR);")
    conn.commit()

    start_time = time.time()
    
    try:
        file = open(file_path, 'r')
    
    except:
        print("error, could not open file.")
        
    my_dict = dict()
    my_set = set()

    start_time = time.time()
    for line in file.readlines():
        word = line[0:-1]
        if(word in my_set):
            if(word in my_dict):
                my_dict[word] = my_dict.get(word) + 1
            else:
                my_dict[word] = 1
        else:
            my_set.add(word)

    data = [(word,) for word in my_set]
    insert_query = 'insert into tokens (token) values %s'
    psycopg2.extras.execute_values (cur, insert_query, data)
    conn.commit()

    print("--- %s seconds ---" % (time.time() - start_time))
    print("length of dictionary = ", len(my_dict))
    print(my_dict)

    cur.close()
    conn.close()
    return
