class Cuts:
    def __init__(self, photon_pt_min = None, photon_pt_tot_IN = None,
                       photon_num = None,    photon_num_min = None,
                       lepton_num = None,    jet_num = None,
                       ptcone_max = None, etcone_max = None, 
                       ptconerel_max = None, etconerel_max = None, 
                       invMass_IN = None,    invMass_EX = None,
                       e_by_invMass = False,
                       photon_eta_exclude = False, 
                       photon_isTight = False,
                       VBF_Enhanced = False):
        self.photon_pt_tot_IN = photon_pt_tot_IN
        self.photon_pt_min = photon_pt_min
        self.photon_num = photon_num
        self.photon_num_min = photon_num_min
        self.lepton_num = lepton_num
        self.jet_num = jet_num
        self.ptcone_max = ptcone_max
        self.etcone_max = etcone_max
        self.ptconerel_max = ptconerel_max
        self.etconerel_max = etconerel_max
        self.invMass_IN = invMass_IN
        self.invMass_EX = invMass_EX
        self.e_by_invMass = e_by_invMass
        self.photon_eta_exclude = photon_eta_exclude
        self.photon_isTight = photon_isTight
        self.VBF_Enhanced = VBF_Enhanced

    def tot_cuts(self):
        cuts_string = ""
        cuts = []
        # Photon transverse energy cut for leading and subleading photons
        if (self.photon_pt_min):
            cuts.append(f"photon_pt[0] >= {self.photon_pt_min[0]}")
            cuts.append(f"photon_pt[1] >= {self.photon_pt_min[1]}")
        # Photon transverse energy for the diphoton system
        if (self.photon_pt_tot_IN):
            cuts.append(f"(photon_pt_tot >= {self.photon_pt_tot_IN[0]} && photon_pt_tot <= {self.photon_pt_tot_IN[1]})")
        # Photon number
        if (self.photon_num is not None): 
            cuts.append(f"photon_n == {self.photon_num}")
        # Minimum photon number
        if (self.photon_num_min is not None):
            cuts.append(f"photon_n >= {self.photon_num_min}")
        # Lepton number
        if (self.lepton_num is not None): 
            cuts.append(f"lep_n == {self.lepton_num}")
        # Jet number
        if (self.jet_num is not None):
            cuts.append(f"jet_n == {self.jet_n}")
        # photon_etcone20 maxmimum
        if (self.etcone_max is not None):
            cuts.append(f"photon_etcone20[0] < {self.etcone_max} && photon_etcone20[1] < {self.etcone_max}")
        if (self.ptconerel_max is not None):
            cuts.append(f"(ptconerel0 < {self.ptconerel_max} && ptconerel1 < {self.ptconerel_max})")
        if (self.etconerel_max is not None):
            cuts.append(f"(etconerel0 < {self.etconerel_max} && etconerel1 < {self.etconerel_max})")
        if (self.invMass_IN is not None):
            cuts.append(f"invMass >= {self.invMass_IN[0]} && invMass <= {self.invMass_IN[1]}")
        if (self.invMass_EX is not None):
            cuts.append(f"(invMass < {self.invMass_EX[0]} || invMass > {self.invMass_EX[1]})")
        if (self.e_by_invMass):
            cuts.append(f"photon_pt[0] / invMass > 0.35 && photon_pt[1] / invMass > 0.25")
        if (self.photon_eta_exclude):
            cuts.append(f"(abs(photon_eta[0]) < 1.37 || abs(photon_eta[0]) > 1.52)")
            cuts.append(f"(abs(photon_eta[1]) < 1.37 || abs(photon_eta[1]) > 1.52)")
        if (self.photon_isTight):
            cuts.append(f"photon_isTightID[0] == 1 && photon_isTightID[1] == 1")
        if (self.VBF_Enhanced):
            cuts.append(f"jet_n == 2 && jet_pt[0] >= 25e3 && jet_pt[1] >= 25e3 && jet_invMass >= 400e3 && \
                          abs(jet_phi[0] - jet_phi[1]) > 2.6")
        if len(cuts) > 0:
            cut_string = " && ".join(cuts)
            
        return cut_string
