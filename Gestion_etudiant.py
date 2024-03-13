class Etudiant:
    def __init__(self, nom, prenom, matricule, adresse, telephone, email, classe):
        #attributs de l'étudiant
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.classe = classe

class EtudiantData:
    def __init__(self):
        self.etudiant = {}

    def ajouter_etudiant(self, etudiant):
        #ajouter un étudiant à la base de données
        self.etudiant[etudiant.matricule] = etudiant

    def supp_etudiant(self, matricule):
        #supprimer un étudiant de la base de données
        if matricule in self.etudiant:
            del self.etudiant[matricule]

    def rechercher_etudiant(self, matricule):
        # pour rechercher un étudiant grace à un matricule
        return self.etudiant.get(matricule, None)

    def modifier_etudiant(self, matricule, etudiant):
        #modifier les détails d'un étudiant
        if matricule in self.etudiant:
            self.etudiant[matricule] = etudiant

    def display_all_students(self):
        #afficher tous les étudiants
        return list(self.etudiant.values())

def main():
    db = EtudiantData()  #base de données des étudiants
    
    while True:
        #menu principal
        print("MENU:")
        print("1. Ajouter un étudiant")
        print("2. Afficher la liste de tous les étudiants")
        print("3. Rechercher un étudiant grace à un matricule")
        print("4. Modifier les détails d'un étudiant existant.")
        print("5. Supprimer un étudiant")

        choix = input("Entrez le numéro de votre choix: ")

        if choix == '1':
            # Ajouter un étudiant
            nom = input("Nom de l'étudiant: ")
            prenom = input("Prénom de l'étudiant: ")
            matricule = input("Matricule de l'étudiant: ")
            adresse = input("Adresse de l'étudiant: ")
            telephone = input("Numéro de téléphone de l'étudiant: ")
            email = input("Email de l'étudiant: ")
            classe = input("Classe de l'étudiant: ")
            nouveau_etudiant = Etudiant(nom, prenom, matricule, adresse, telephone, email, classe)
            db.ajouter_etudiant(nouveau_etudiant)
            print("Étudiant ajouté!")

        elif choix == '2':
            # Afficher la liste de tous les étudiants
            etudiant = db.display_all_students()
            print("Liste de tous les étudiants:")
            for etudiant in etudiant:
                print(vars(etudiant))

        elif choix == '3':
            # Rechercher un étudiant grace à un matricule
            matricule = input("Entrez le matricule de l'étudiant que vous recherchez: ")
            etudiant = db.rechercher_etudiant(matricule)
            if etudiant:
                print("L'Étudiant a été trouvé:")
                print(vars(etudiant))
            else:
                print("Aucun étudiant a été trouvé avec ce matricule.")

        elif choix == '4':
            # Modifier les détails d'un étudiant
            matricule = input("Entrez le matricule de l'étudiant à modifier: ")
            etudiant = db.rechercher_etudiant(matricule)
            if etudiant:
                print("L'Étudiant trouvé:")
                print(vars(etudiant))
                nom = input("Nouveau nom (Ne mettez rien pour ne pas modifier): ")
                prenom = input("Nouveau prénom (Ne mettez rien pour ne pas modifier): ")
                adresse = input("Nouvelle adresse (Ne mettez rien pour ne pas modifier): ")
                telephone = input("Nouveau numéro de téléphone (Ne mettez rien pour ne pas modifier): ")
                email = input("Nouvel email (Ne mettez rien pour ne pas modifier): ")
                classe = input("Nouvelle classe (Ne mettez rien pour ne pas modifier): ")
                if nom or prenom or adresse or telephone or email or classe:
                    modifié_etudiant = Etudiant(nom or etudiant.nom, prenom or etudiant.prenom, matricule, adresse or etudiant.adresse, telephone or etudiant.telephone, email or etudiant.email, classe or etudiant.classe)
                    db.modifier_etudiant(matricule, modifié_etudiant)
                    print("Détails de l'étudiant mis à jour!")
                else:
                    print("Aucune modification effectuée.")
            else:
                print("Aucun étudiant trouvé avec ce matricule/identifiant.")

        elif choix == '5':
            # Supprimer un étudiant
            matricule = input("Entrez le matricule de l'étudiant à supprimer: ")
            confirmer = input("Êtes-vous sûr de vouloir supprimer cet étudiant ? (Oui ou Non): ")
            if confirmer.upper() == 'Oui':
                db.supp_etudiant(matricule)
                print("Étudiant supprimé avec succès!")
            else:
                print("Pas de suppression.")

        else:
            print("Choix invalide. Veuillez entrer un numéro de choix valide.")

if __name__ == "__main__":
    main()
