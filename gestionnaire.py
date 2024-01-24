from tache import Tache

class GestionnaireTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, nom):
        nouvelle_tache = Tache(nom)
        self.taches.append(nouvelle_tache)

    def supprimer_tache(self, nom):
        tache_a_supprimer = None
        for tache in self.taches:
            if tache.nom == nom:
                tache_a_supprimer = tache
                break

        if tache_a_supprimer:
            self.taches.remove(tache_a_supprimer)
            print(f"Tâche '{nom}' supprimée avec succès.")
        else:
            print(f"Tâche '{nom}' introuvable.")

    def marquer_tache_terminée(self, nom):
        for tache in self.taches:
            if tache.nom == nom:
                tache.terminee = True
                print(f"Tâche '{nom}' marquée comme terminée.")
                return

        print(f"Tâche '{nom}' introuvable.")

    def liste_taches_en_cours(self):
        print("Tâches en cours :")
        for tache in self.taches:
            if not tache.terminee:
                print(f"- {tache.nom}")

