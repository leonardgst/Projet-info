import psycopg2
import requests
import gzip
import json



def main():
    conn=None
    cur=None
    try:
        ###Connexion au serveur 
        conn = psycopg2.connect(host='localhost',

                    dbname = 'UTILISATEUR',
                    user = 'postgres',
                    password = '56992711',
                    port = 5432)
        cur = conn.cursor()
        ###Creation de la table
        create_script='''
        CREATE TABLE utilisateur (
                                id_user SERIAL PRIMARY KEY NOT NULL,
                                
                                mail VARCHAR(50),
                                MDP VARCHAR(50),
                                dateNaissance VARCHAR(50),
                                nom VARCHAR(50),
                                prenom VARCHAR(50)
                                );'''
                                        
        cur.execute(create_script)
        

    except Exception as error : 
            print(error)
    finally : 
        ###déconnexion + arrêt curseur
            if cur is not None:
                cur.close()
            if conn is not None :
                conn.close()

if __name__ == "__main__":
    main()