
def test_une_equipe_a_un_nom_et_une_promo(db):
    equipe=Equipe.objects.create(nom="Les Lions",promo="L1")
    assert equipe.nom
    assert equipe.promo