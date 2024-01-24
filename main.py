from gestionnaire import GestionnaireTaches

def main():
    gestionnaire = GestionnaireTaches()

    while True:
        print("Gestionnaire de tâches")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Marquer une tâche comme terminée")
        print("4. Liste des tâches en cours")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            tache = input("Entrez le nom de la tâche : ")
            gestionnaire.ajouter_tache(tache)
        elif choix == "2":
            tache = input("Entrez le nom de la tâche à supprimer : ")
            gestionnaire.supprimer_tache(tache)
        elif choix == "3":
            tache = input("Entrez le nom de la tâche terminée : ")
            gestionnaire.marquer_tache_terminée(tache)
        elif choix == "4":
            gestionnaire.liste_taches_en_cours()
        elif choix == "5":
            break
        else:
            print("Option invalide. Réessayez.")

if __name__ == "__main__":
    main()
