def montage(devant_droit, manche, dos, devant_gauche):
    instruction = "Debut : monter " + str(devant_droit) + " mailles, placer un marqueur, 1 maille, placer un marqueur, " + str(manche) + " mailles, placer un marqueur, 1 maille, placer un marqueur, " + str(dos) + " mailles, placer un marqueur, 1 maille, placer un marqueur, " + str(manche) + " mailles, placer un marqueur, 1 maille, placer un marqueur, " + str(devant_gauche) + " mailles.\n"

    return instruction

def rangsAplat(rangs):
    instruction = "il faut tricoter a plat pendant " + str(rangs) + " rangs.\n"
    return instruction