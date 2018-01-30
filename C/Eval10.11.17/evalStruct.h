struct noeud {
    char * nom;
    struct noeud * nextNoeud;
};

struct lien {
    int cout;
    struct lien * nextLien;
    struct noeud * debut;
    struct noeud * fin;
};

struct graphe {
    
    struct noeud * pointEntree;
    struct lien * lienEntree;

};
