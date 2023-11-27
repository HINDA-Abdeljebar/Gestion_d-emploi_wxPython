import sqlite3

# Initialiser la connexion à la base de données et le curseur
conn = sqlite3.connect('myDataBase.db')
cursor = conn.cursor()

# Créer des tableaux s'ils n'existent pas
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Utilisateur (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            prenom TEXT,
            role TEXT,
            email TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cours (
            id INTEGER PRIMARY KEY,
            nom_cours TEXT,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EmploiDuTemps (
            id INTEGER PRIMARY KEY,
            jour_semaine TEXT,
            heure_debut TEXT,
            heure_fin TEXT,
            cours_id INTEGER,
            utilisateur_id INTEGER,
            salle_id INTEGER,
            FOREIGN KEY (cours_id) REFERENCES Cours(id),
            FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id),
            FOREIGN KEY (salle_id) REFERENCES Salle(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salle (
            id INTEGER PRIMARY KEY,
            nom_salle TEXT,
            capacite INTEGER
        )
    ''')

    conn.commit()

# des Fonctions CRUD pour Utilisateur 
def create_utilisateur(id, nom, prenom, role, email):
    cursor.execute('INSERT INTO Utilisateur (id, nom, prenom, role, email) VALUES (?, ?, ?, ?, ?)', (id, nom, prenom, role, email))
    conn.commit()

def get_all_utilisateurs():
    cursor.execute('SELECT * FROM Utilisateur')
    utilisateurs = cursor.fetchall()
    return utilisateurs

def update_utilisateur(id, nom, prenom, role, email):
    cursor.execute("UPDATE Utilisateur SET nom = ?, prenom = ?, role = ?, email = ? WHERE id = ?", (nom, prenom, role, email, id))
    conn.commit()

def delete_utilisateur(utilisateur_id):
    cursor.execute('DELETE FROM Utilisateur WHERE id = ?', (utilisateur_id,))
    conn.commit()

#  des functions CRUD pour les Cours 
def create_cours(nom_cours, description):
    cursor.execute('INSERT INTO Cours (nom_cours, description) VALUES (?, ?)', (nom_cours, description))
    conn.commit()

def get_all_cours():
    cursor.execute('SELECT * FROM Cours')
    cours = cursor.fetchall()
    return cours

def update_cours_description(cours_id,nom_cours, new_description):
    cursor.execute('UPDATE Cours SET description = ?,nom_cours = ? WHERE id = ?', (nom_cours,new_description, cours_id))
    conn.commit()

def delete_cours(cours_id):
    cursor.execute('DELETE FROM Cours WHERE id = ?', (cours_id,))
    conn.commit()


# des functions CRUD  pour les Salles
def create_salle(nom_salle, capacite):
    cursor.execute('INSERT INTO Salle (nom_salle, capacite) VALUES (?, ?)', (nom_salle, capacite))
    conn.commit()

def get_all_salles():
    cursor.execute('SELECT * FROM Salle')
    salles = cursor.fetchall()
    return salles

def update_salle_capacite(salle_id, new_capacite):
    cursor.execute('UPDATE Salle SET capacite = ? WHERE id = ?', (new_capacite, salle_id))
    conn.commit()

def delete_salle(salle_id):
    cursor.execute('DELETE FROM Salle WHERE id = ?', (salle_id,))
    conn.commit()


# des functions CRUD  pour les EmploiDuTemps 

def create_emploidutemps(jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id):
    cursor.execute('INSERT INTO EmploiDuTemps (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id) VALUES (?, ?, ?, ?, ?, ?)', (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id))
    conn.commit()

def get_all_emploidutemps():
    cursor.execute('SELECT * FROM EmploiDuTemps')
    emploidutemps = cursor.fetchall()
    return emploidutemps

def update_emploidutemps(emploi_id, jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id):
    cursor.execute('UPDATE EmploiDuTemps SET jour_semaine = ?, heure_debut = ?, heure_fin = ?, cours_id = ?, utilisateur_id = ?, salle_id = ? WHERE id = ?', (jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id, emploi_id))
    conn.commit()

def delete_emploidutemps(emploi_id):
    cursor.execute('DELETE FROM EmploiDuTemps WHERE id = ?', (emploi_id,))
    conn.commit()

