import sqlite3




def connect(db_path):
    conn = sqlite3.connect(db_path)
    cursor=conn.cursor()
    return conn, cursor


def create_users_table():
    conn, cursor=connect('../translation.db')
    sql="""
        create table if not exists bot_users(
            user_id integer primary key autoincrement,
            chat_id bigint not null
    
        );
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()


def create_translations_table():
    conn, cursor=connect('../translation.db')
    sql="""
        create table if not exists translations(
            translation_id integer primary key autoincrement,
            original text not null,
            translated text not null,
            code_from text not null,
            code_to text not null,
            user_id integer references bot_users(user_id)    
        
        )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()




# create_users_table()
# create_translations_table()


def get_user_id(chat_id):
    conn, cursor = connect('translation.db')
    sql='select user_id from bot_users where chat_id=?'
    user_id=cursor.execute(sql, (chat_id,)).fetchone()
    if user_id is None:
        return 0, False
    return user_id[0], True


def add_user(chat_id):
    C
    cursor.execute(sql, (chat_id,))
    conn.commit()
    conn.close()
    print(f'Added user with id: {chat_id}')


def add_translation(original, translated, code_from, code_to, chat_id):
    user_id, exists=get_user_id(chat_id)
    conn, cursor = connect('translation.db')
    sql='''
        insert into translations(original, translated, code_from, code_to, user_id) values(?, ?, ?, ?, ?)
    '''
    cursor.execute(sql, (original, translated, code_from, code_to, user_id))
    conn.commit()
    conn.close()
    print(f'Translation added')



def get_history(chat_id):
    conn, cursor = connect('translation.db')
    sql='select * from translations where user_id=?'
    user_id=get_user_id(chat_id)
    cursor.execute(sql, (user_id, ))
    records=cursor.fetchall()
    print(record)
    conn.close()
    return records















