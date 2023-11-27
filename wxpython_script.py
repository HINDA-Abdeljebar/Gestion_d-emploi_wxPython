import wx
from db_methodes import *
class App(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(700, 450))
        
        self.panel = wx.Panel(self)
        self.notebook = wx.Notebook(self.panel)
        
        self.home_tab = wx.Panel(self.notebook)
        self.utilisateurs_tab = wx.Panel(self.notebook)
        self.cours_tab = wx.Panel(self.notebook)
        self.salles_tab = wx.Panel(self.notebook)
        self.emploi_tab = wx.Panel(self.notebook)
        
        self.notebook.AddPage(self.home_tab, "Home")
        self.notebook.AddPage(self.utilisateurs_tab, "Gestion d'utilisateurs")
        self.notebook.AddPage(self.cours_tab, "Gestion de Cours")
        self.notebook.AddPage(self.salles_tab, "Gestion de Salles")
        self.notebook.AddPage(self.emploi_tab, "Gestion d'emploi de temps")
        self.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        
        self.load_tab_content(0) 
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        
        self.Centre()
        self.Show()
        
    def on_tab_change(self, event):
        selection = event.GetSelection()
        self.load_tab_content(selection)
        
    def clear_frame(self, tab):
        sizer = tab.GetSizer()
        if sizer:
            sizer.Clear(True)
            tab.SetSizer(sizer)
            tab.Layout()  
              
    def load_tab_content(self, index):
        if index == 0:
            self.home()
        elif index == 1:
            self.utilisateurs()
        elif index == 2:
            self.cours()
        elif index == 3:
            self.salles()
        elif index == 4:
            self.emploi()
    # page d'acceuil    
    def home(self):
        self.clear_frame(self.home_tab)
        text = wx.StaticText(self.home_tab, label="Welcome to the Home tab")
        font = text.GetFont()
        font.MakeBold()
        text.SetFont(font)
        text.SetForegroundColour(wx.BLUE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALIGN_CENTER)
        self.home_tab.SetSizer(sizer)
    # utilisateur tap   
    def utilisateurs(self):
        self.clear_frame(self.utilisateurs_tab)
        form_layout = wx.BoxSizer(wx.VERTICAL)
        self.utilisateurs_tab.SetSizer(form_layout)

        frame_title = wx.StaticText(self.utilisateurs_tab, label="Gestion d'utilisateurs :")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        frame_title.SetForegroundColour(wx.BLUE)
        form_layout.Add(frame_title, 0, wx.ALIGN_CENTER)

        grid_sizer = wx.GridSizer(rows=4, cols=1, vgap=10, hgap=10)  

        list_button = wx.Button(self.utilisateurs_tab, label="Liste des Utilisateurs")
        list_button.Bind(wx.EVT_BUTTON, self.display_utilisateurs)
        grid_sizer.Add(list_button, 0, wx.EXPAND)

        add_button = wx.Button(self.utilisateurs_tab, label="Ajouter Utilisateur")
        add_button.Bind(wx.EVT_BUTTON, self.add_utilisateur)
        grid_sizer.Add(add_button, 0, wx.EXPAND)

        edit_button = wx.Button(self.utilisateurs_tab, label="Editer Utilisateur")
        edit_button.Bind(wx.EVT_BUTTON, self.update_utilisateur)
        grid_sizer.Add(edit_button, 0, wx.EXPAND)

        delete_button = wx.Button(self.utilisateurs_tab, label="Supprimer Utilisateurs")
        delete_button.Bind(wx.EVT_BUTTON, self.delete_utilisateur)
        grid_sizer.Add(delete_button, 0, wx.EXPAND)

        form_layout.Add(grid_sizer, 0, wx.EXPAND | wx.ALL, 20)  
        form_layout.Layout()
        self.utilisateurs_tab.Layout()

        
    # afficher les utilisateurs
    def display_utilisateurs(self, event):
        self.clear_frame(self.utilisateurs_tab)
        utilisateurs = get_all_utilisateurs()

        table = wx.ListCtrl(self.utilisateurs_tab, style=wx.LC_REPORT)
        table.InsertColumn(0, "ID" , width=110)
        table.InsertColumn(1, "Nom" , width=110)
        table.InsertColumn(2, "Prénom" , width=110)
        table.InsertColumn(3, "Rôle" , width=110)
        table.InsertColumn(4, "Email" , width=210)

        for index, utilisateur in enumerate(utilisateurs):
            table.InsertItem(index, str(utilisateur[0]))
            table.SetItem(index, 1, utilisateur[1])
            table.SetItem(index, 2, utilisateur[2])
            table.SetItem(index, 3, utilisateur[3])
            table.SetItem(index, 4, utilisateur[4])    
               
        home_btn = wx.Button(self.utilisateurs_tab, label="Retour")
        home_btn.Bind(wx.EVT_BUTTON , self.utilisateurs)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(table, 1, wx.EXPAND | wx.ALL, border=10)
        sizer.Add(home_btn, 0, wx.ALIGN_CENTER | wx.ALL, border=10)
                
        self.utilisateurs_tab.SetSizer(sizer)
        self.utilisateurs_tab.Layout() 
        self.Layout()  
        

    # Ajouter un utlisateurs
    def add_utilisateur(self, event):
        self.clear_frame(self.utilisateurs_tab)
        
        form_frame = wx.Panel(self.utilisateurs_tab)
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_frame.SetSizer(form_sizer)
        
        grid_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, border=10)
        
        id_label = wx.StaticText(form_frame, label="Id:")
        self.id_entry = wx.TextCtrl(form_frame)
        grid_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        grid_sizer.Add(self.id_entry, 0, wx.EXPAND)
        
        nom_label = wx.StaticText(form_frame, label="Nom:")
        self.nom_entry = wx.TextCtrl(form_frame)
        grid_sizer.Add(nom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        grid_sizer.Add(self.nom_entry, 0, wx.EXPAND)
        
        prenom_label = wx.StaticText(form_frame, label="Prénom:")
        self.prenom_entry = wx.TextCtrl(form_frame)
        grid_sizer.Add(prenom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        grid_sizer.Add(self.prenom_entry, 0, wx.EXPAND)
        
        role_label = wx.StaticText(form_frame, label="Rôle:")
        self.role_entry = wx.TextCtrl(form_frame)
        grid_sizer.Add(role_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        grid_sizer.Add(self.role_entry, 0, wx.EXPAND)
        
        email_label = wx.StaticText(form_frame, label="Email:")
        self.email_entry = wx.TextCtrl(form_frame)
        grid_sizer.Add(email_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        grid_sizer.Add(self.email_entry, 0, wx.EXPAND)
        
        button_submit = wx.Button(form_frame, label="Ajouter")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_form)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=10)
        
        sizer = self.utilisateurs_tab.GetSizer()
        if sizer:
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
            self.utilisateurs_tab.SetSizer(sizer)
        self.utilisateurs_tab.Layout()

    # ajouter a BD
    def submit_form(self, event):
        id = self.id_entry.GetValue()
        nom = self.nom_entry.GetValue()
        prenom = self.prenom_entry.GetValue()
        role = self.role_entry.GetValue()
        email = self.email_entry.GetValue()
        
        create_utilisateur(id, nom, prenom, role, email)
        self.clear_frame(self.utilisateurs_tab)
        self.utilisateurs() 
        
    # mise a jour un utilisateur
    def update_utilisateur(self, event):
        self.clear_frame(self.utilisateurs_tab)
        
        form_frame = wx.Panel(self.utilisateurs_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_frame.SetSizer(form_sizer)
        
        id_label = wx.StaticText(form_frame, label="Id:")
        self.id_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND)
        
        nom_label = wx.StaticText(form_frame, label="Nom:")
        self.nom_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(nom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.nom_entry, 0, wx.EXPAND)
        
        prenom_label = wx.StaticText(form_frame, label="Prénom:")
        self.prenom_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(prenom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.prenom_entry, 0, wx.EXPAND)
        
        role_label = wx.StaticText(form_frame, label="Rôle:")
        self.role_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(role_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.role_entry, 0, wx.EXPAND)
        
        email_label = wx.StaticText(form_frame, label="Email:")
        self.email_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(email_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.email_entry, 0, wx.EXPAND)
        
        button_submit = wx.Button(form_frame, label="Update")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_update)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=10)
        
        sizer = self.utilisateurs_tab.GetSizer()
        if sizer:
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
            self.utilisateurs_tab.SetSizer(sizer)
        self.utilisateurs_tab.Layout()

    def submit_update(self, event):
        id = self.id_entry.GetValue()
        nom = self.nom_entry.GetValue()
        prenom = self.prenom_entry.GetValue()
        role = self.role_entry.GetValue()
        email = self.email_entry.GetValue()
        
        result = update_utilisateur(id, nom, prenom, role, email)  
        
        if result == 0:
            print("Utilisateur introuvable, mise à jour non effectuée")
        else:
            self.clear_frame(self.utilisateurs_tab)
            self.utilisateurs()  
    # supprimer un utilisateur
    def delete_utilisateur(self, event):
        self.clear_frame(self.utilisateurs_tab)
        
        form_frame = wx.Panel(self.utilisateurs_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_frame.SetSizer(form_sizer)
        
        id_label = wx.StaticText(form_frame, label="Id:")
        self.id_entry = wx.TextCtrl(form_frame)
        form_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND)
        
        button_submit = wx.Button(form_frame, label="Delete")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_delete)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)
        
        sizer = self.utilisateurs_tab.GetSizer()
        if sizer:
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_frame, 1, wx.EXPAND | wx.ALL, border=5)
            self.utilisateurs_tab.SetSizer(sizer)
        self.utilisateurs_tab.Layout()

    def submit_delete(self, event):
        id = self.id_entry.GetValue()
        delete_utilisateur(id)  
        
        self.clear_frame(self.utilisateurs_tab)
        self.utilisateurs(None)  

    ## les cours
    def cours(self):
        self.clear_frame(self.cours_tab)
        form_layout = wx.BoxSizer(wx.VERTICAL)
        self.cours_tab.SetSizer(form_layout)
        
        frame_title = wx.StaticText(self.cours_tab, label="Gestion de Cours :")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        frame_title.SetForegroundColour(wx.BLUE)
        form_layout.Add(frame_title, 0, wx.ALIGN_CENTER)
        
        grid_sizer = wx.GridSizer(rows=4, cols=1, vgap=10, hgap=10)  
        
        list_button = wx.Button(self.cours_tab, label="Liste des Cours")
        list_button.Bind(wx.EVT_BUTTON, self.display_cours)
        grid_sizer.Add(list_button, 0, wx.EXPAND)
        
        add_button = wx.Button(self.cours_tab, label="Ajouter Cours")
        add_button.Bind(wx.EVT_BUTTON, self.add_cours)
        grid_sizer.Add(add_button, 0, wx.EXPAND)
        
        edit_button = wx.Button(self.cours_tab, label="Editer Cours")
        edit_button.Bind(wx.EVT_BUTTON, self.update_cours)
        grid_sizer.Add(edit_button, 0, wx.EXPAND)
        
        delete_button = wx.Button(self.cours_tab, label="Supprimer Cours")
        delete_button.Bind(wx.EVT_BUTTON, self.delete_cours)
        grid_sizer.Add(delete_button, 0, wx.EXPAND)
        
        form_layout.Add(grid_sizer, 0, wx.EXPAND | wx.ALL, 20)  # Add the grid sizer to the main sizer
        form_layout.Layout()
        self.cours_tab.Layout()

    # afficher les cours  
    def display_cours(self, event):
        self.clear_frame(self.cours_tab)
        cours = get_all_cours()

        table = wx.ListCtrl(self.cours_tab, style=wx.LC_REPORT)
        table.InsertColumn(0, "ID",  width=120)
        table.InsertColumn(1, "Nom",  width=120)
        table.InsertColumn(2, "Description" , width=200)

        for index, cour in enumerate(cours):
            table.InsertItem(index, str(cour[0]))
            table.SetItem(index, 1, cour[1])
            table.SetItem(index, 2, cour[2])

        home_btn = wx.Button(self.cours_tab, label="Retour")
        home_btn.Bind(wx.EVT_BUTTON, self.cours)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(table, 1, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(home_btn, 0, wx.ALIGN_CENTER | wx.ALL, border=5)
        
        self.cours_tab.SetSizer(sizer)
        self.cours_tab.Layout()
        
    # ajouter un cours
    def add_cours(self, event):
        self.clear_frame(self.cours_tab)

        form_panel = wx.Panel(self.cours_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        nom_label = wx.StaticText(form_panel, label="Nom:")
        self.nom_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(nom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.nom_entry, 0, wx.EXPAND)

        description_label = wx.StaticText(form_panel, label="Description:")
        self.description_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(description_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.description_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Ajouter")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_form_cours)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer = self.cours_tab.GetSizer()
        if sizer:
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
            self.cours_tab.SetSizer(sizer)
        self.cours_tab.Layout()

    def submit_form_cours(self, event):
        nom = self.nom_entry.GetValue()
        description = self.description_entry.GetValue()
        create_cours(nom, description)
        
        self.clear_frame(self.cours_tab)
        self.cours() 
    # mise a jour d'un cours
    def update_cours(self, event):
        self.clear_frame(self.cours_tab)

        form_panel = wx.Panel(self.cours_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        frame_title = wx.StaticText(form_panel, label="Update Cours")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER_VERTICAL)

        id_label = wx.StaticText(form_panel, label="Id:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND)

        nom_label = wx.StaticText(form_panel, label="nom_cours:")
        self.nom_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(nom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.nom_entry, 0, wx.EXPAND)

        description_label = wx.StaticText(form_panel, label="description :")
        self.description_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(description_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.description_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Update")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_update)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer = self.cours_tab.GetSizer()
        if sizer:
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
            self.cours_tab.SetSizer(sizer)
        self.cours_tab.Layout()

    def submit_update(self, event):
        id = self.id_entry.GetValue()
        nom_cours = self.nom_entry.GetValue()
        description = self.description_entry.GetValue()
        result = update_cours_description(id, nom_cours, description)

        if result == 0:
            print("Cours introuvable, mise à jour non effectuée")
        else:
            self.clear_frame(self.utilisateurs_tab)
            self.cours(None)
    
    #  supprimer d'un cours
    def delete_cours(self, event):
        self.clear_frame(self.cours_tab)

        form_panel = wx.Panel(self.cours_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        frame_title = wx.StaticText(form_panel, label="Delete Cours")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER_VERTICAL)

        id_label = wx.StaticText(form_panel, label="Id:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Delete")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_delete_cours)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer = self.cours_tab.GetSizer()
        if sizer:
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
            self.cours_tab.SetSizer(sizer)
        self.cours_tab.Layout()

    def submit_delete_cours(self, event):
        id = self.id_entry.GetValue()
        delete_cours(id)
        self.clear_frame(self.cours_tab)
        self.cours(None)

    ## les salles  
    def salles(self):
        self.clear_frame(self.salles_tab)
        form_layout_salles = wx.BoxSizer(wx.VERTICAL)
        self.salles_tab.SetSizer(form_layout_salles)

        frame_title = wx.StaticText(self.salles_tab, label="Gestion des salles :")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        frame_title.SetForegroundColour(wx.BLUE)
        form_layout_salles.Add(frame_title, 0, wx.ALIGN_CENTER)

        grid_sizer = wx.GridSizer(rows=4, cols=1, vgap=10, hgap=10)  # Create a grid sizer

        list_button = wx.Button(self.salles_tab, label="Liste des Salles")
        list_button.Bind(wx.EVT_BUTTON, self.display_salles)
        grid_sizer.Add(list_button, 0, wx.EXPAND)

        add_button = wx.Button(self.salles_tab, label="Ajouter Salles")
        add_button.Bind(wx.EVT_BUTTON, self.add_salles)
        grid_sizer.Add(add_button, 0, wx.EXPAND)

        edit_button = wx.Button(self.salles_tab, label="Editer Salles")
        edit_button.Bind(wx.EVT_BUTTON, self.update_salle)
        grid_sizer.Add(edit_button, 0, wx.EXPAND)

        delete_button = wx.Button(self.salles_tab, label="Supprimer Salles")
        delete_button.Bind(wx.EVT_BUTTON, self.delete_salle)
        grid_sizer.Add(delete_button, 0, wx.EXPAND)

        form_layout_salles.Add(grid_sizer, 0, wx.EXPAND | wx.ALL, 20)  # Add the grid sizer to the main sizer
        form_layout_salles.Layout()
        self.salles_tab.Layout()

    
    # afficher les salles
    def display_salles(self, event):
        self.clear_frame(self.salles_tab)
        salles = get_all_salles()

        table = wx.ListCtrl(self.salles_tab, style=wx.LC_REPORT)
        table.InsertColumn(0, "ID", width=120)
        table.InsertColumn(1, "Nom", width=120)
        table.InsertColumn(2, "Capacite", width=200)

        for index, salle in enumerate(salles):
            table.InsertItem(index, str(salle[0]))
            table.SetItem(index, 1, salle[1])
            table.SetItem(index, 2, str(salle[2]))

        home_btn = wx.Button(self.salles_tab, label="Retour")
        home_btn.Bind(wx.EVT_BUTTON, self.salles)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(table, 1, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(home_btn, 0, wx.ALIGN_CENTER | wx.ALL, border=5)

        self.salles_tab.SetSizer(sizer)
        self.salles_tab.Layout()

    # ajouter des salles
    def add_salles(self, event):
        self.clear_frame(self.salles_tab)

        form_panel = wx.Panel(self.salles_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        nom_label = wx.StaticText(form_panel, label="Nom Salle:")
        self.nom_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(nom_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.nom_entry, 0, wx.EXPAND)

        capacite_label = wx.StaticText(form_panel, label="Capacite:")
        self.capacite_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(capacite_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.capacite_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Ajouter")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_form_salle)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer = self.salles_tab.GetSizer()
        if sizer:
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
            self.salles_tab.SetSizer(sizer)
        self.salles_tab.Layout()

    def submit_form_salle(self, event):
        nom_salle = self.nom_entry.GetValue()
        capacite = self.capacite_entry.GetValue()
        create_salle(nom_salle, capacite)
        self.clear_frame(self.salles_tab)
        self.salles()
        
    # mise a jour des salles
    def update_salle(self):
        self.clear_frame(self.salles_tab)

        form_panel = wx.Panel(self.salles_tab)
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_panel.SetSizer(form_sizer)
        self.salles_tab.GetSizer().Add(form_panel, 1, wx.EXPAND)

        frame_title = wx.StaticText(form_panel, label="Mise à jour Salle")
        frame_title.SetFont(wx.Font(wx.FontInfo(12).Bold()))
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        id_label = wx.StaticText(form_panel, label="ID:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND | wx.ALL, 5)

        nom_label = wx.StaticText(form_panel, label="Nom Salle:")
        self.nom_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(nom_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.nom_entry, 0, wx.EXPAND | wx.ALL, 5)

        capacite_label = wx.StaticText(form_panel, label="Capacité:")
        self.capacite_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(capacite_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.capacite_entry, 0, wx.EXPAND | wx.ALL, 5)

        button_submit = wx.Button(form_panel, label="Mettre à jour")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_update)
        form_sizer.Add(button_submit, 0, wx.EXPAND | wx.ALL, 5)

    def submit_update(self, event):
        id = self.id_entry.GetValue()
        nom_salle = self.nom_entry.GetValue()
        capacite = self.capacite_entry.GetValue()
        result = update_salle_info(id, nom_salle, capacite)
        if result == 0:
            print("Salle introuvable, mise à jour non effectuée")
        else:
            self.clear_frame(self.salles_tab)
            self.salle()  

    # supprimer d'un salle
    def delete_salle(self, event):
        self.clear_frame(self.salles_tab)

        form_panel = wx.Panel(self.salles_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        frame_title = wx.StaticText(form_panel, label="Delete Salle")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER_VERTICAL)

        id_label = wx.StaticText(form_panel, label="Id:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Delete")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_delete_salle)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer = self.salles_tab.GetSizer()
        if sizer:
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        else:
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
            self.salles_tab.SetSizer(sizer)
        self.salles_tab.Layout()

    def submit_delete_salle(self, event):
        id = self.id_entry.GetValue()
        delete_salle(id)
        self.clear_frame(self.salles_tab)
        self.salle(None)

    

    ## emploi du temps   
    def emploi(self):
        self.clear_frame(self.emploi_tab)
        existing_layout = self.emploi_tab.GetSizer()
        if existing_layout:
            self.emploi_tab.SetSizer(existing_layout)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.emploi_tab.SetSizer(sizer)

        frame_title = wx.StaticText(self.emploi_tab, label="Gestion d'Emplois :")
        font = frame_title.GetFont()
        font.MakeBold()
        frame_title.SetFont(font)
        frame_title.SetForegroundColour(wx.BLUE)
        sizer.Add(frame_title, 0, wx.ALIGN_CENTER)

        grid_sizer = wx.GridSizer(rows=4, cols=1, vgap=10, hgap=10)  # Create a grid sizer

        list_button = wx.Button(self.emploi_tab, label="Liste des Emplois")
        list_button.Bind(wx.EVT_BUTTON, self.display_emploi)
        grid_sizer.Add(list_button, 0, wx.EXPAND)

        add_button = wx.Button(self.emploi_tab, label="Ajouter Emploi")
        add_button.Bind(wx.EVT_BUTTON, self.add_emploi)
        grid_sizer.Add(add_button, 0, wx.EXPAND)

        edit_button = wx.Button(self.emploi_tab, label="Editer Emploi")
        edit_button.Bind(wx.EVT_BUTTON, self.update_emploi)
        grid_sizer.Add(edit_button, 0, wx.EXPAND)

        delete_button = wx.Button(self.emploi_tab, label="Supprimer Emploi")
        delete_button.Bind(wx.EVT_BUTTON, self.delete_emploi)
        grid_sizer.Add(delete_button, 0, wx.EXPAND)

        sizer.Add(grid_sizer, 0, wx.EXPAND | wx.ALL, 20)  # Add the grid sizer to the main sizer
        self.emploi_tab.Layout()

    # afficher des emplois
    def display_emploi(self, event):
        self.clear_frame(self.emploi_tab)
        emploidutemps = get_all_emploidutemps()

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.emploi_tab.SetSizer(sizer)

        table = wx.ListCtrl(self.emploi_tab, style=wx.LC_REPORT)
        table.InsertColumn(0, "ID")
        table.InsertColumn(1, "Jour de la semaine" , width = 130)
        table.InsertColumn(2, "Heure de début" , width = 130)
        table.InsertColumn(3, "Heure de fin")
        table.InsertColumn(4, "Cours ID")
        table.InsertColumn(5, "Utilisateur ID")
        table.InsertColumn(6, "Salle ID")
        sizer.Add(table, 1, wx.EXPAND | wx.ALL, border=5)

        for index, emploi in enumerate(emploidutemps):
            table.InsertItem(index, str(emploi[0]))
            table.SetItem(index, 1, emploi[1])
            table.SetItem(index, 2, emploi[2])
            table.SetItem(index, 3, emploi[3])
            table.SetItem(index, 4, str(emploi[4]))
            table.SetItem(index, 5, str(emploi[5]))
            table.SetItem(index, 6, str(emploi[6]))

        home_btn = wx.Button(self.emploi_tab, label="Retour")
        home_btn.Bind(wx.EVT_BUTTON, self.emploi)
        sizer.Add(home_btn, 0, wx.ALIGN_CENTER | wx.ALL, border=5)
        self.emploi_tab.Layout()

    # ajouter des emplois
    def add_emploi(self, event):
        self.clear_frame(self.emploi_tab)
        
        form_panel = wx.Panel(self.emploi_tab)
        form_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        form_panel.SetSizer(form_sizer)

        jour_semaine_label = wx.StaticText(form_panel, label="Jour de la semaine:")
        self.jour_semaine_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(jour_semaine_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.jour_semaine_entry, 0, wx.EXPAND)

        heure_debut_label = wx.StaticText(form_panel, label="Heure de début:")
        self.heure_debut_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(heure_debut_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.heure_debut_entry, 0, wx.EXPAND)

        heure_fin_label = wx.StaticText(form_panel, label="Heure de fin:")
        self.heure_fin_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(heure_fin_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.heure_fin_entry, 0, wx.EXPAND)

        cours_id_label = wx.StaticText(form_panel, label="Cours ID:")
        self.cours_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(cours_id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.cours_id_entry, 0, wx.EXPAND)

        utilisateur_id_label = wx.StaticText(form_panel, label="Utilisateur ID:")
        self.utilisateur_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(utilisateur_id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.utilisateur_id_entry, 0, wx.EXPAND)

        salle_id_label = wx.StaticText(form_panel, label="Salle ID:")
        self.salle_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(salle_id_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.salle_id_entry, 0, wx.EXPAND)

        button_submit = wx.Button(form_panel, label="Ajouter")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_form_emploi)
        form_sizer.Add(button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        
        sizer = self.emploi_tab.GetSizer()
        if not sizer:
            sizer = wx.BoxSizer(wx.VERTICAL)
            self.emploi_tab.SetSizer(sizer)
        
        sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, border=5)
        self.emploi_tab.Layout()



    def submit_form_emploi(self, event):
        jour_semaine = self.jour_semaine_entry.GetValue()
        heure_debut = self.heure_debut_entry.GetValue()
        heure_fin = self.heure_fin_entry.GetValue()
        cours_id = self.cours_id_entry.GetValue()
        utilisateur_id = self.utilisateur_id_entry.GetValue()
        salle_id = self.salle_id_entry.GetValue()

        create_emploidutemps(jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id)
        self.clear_frame(self.emploi_tab)
        self.emploi() 
        
    # mise a jour d'un emploi 
    def update_emploi(self):
        self.clear_frame(self.emploi_tab)
        form_panel = wx.Panel(self.emploi_tab)
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_panel.SetSizer(form_sizer)
        self.emploi_tab.GetSizer().Add(form_panel, 1, wx.EXPAND)

        frame_title = wx.StaticText(form_panel, label="Mise à jour d'emploi du temps")
        frame_title.SetFont(wx.Font(wx.FontInfo(12).Bold()))
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        id_label = wx.StaticText(form_panel, label="ID de l'emploi du temps à mettre à jour:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND | wx.ALL, 5)

        jour_semaine_label = wx.StaticText(form_panel, label="Nouveau jour de la semaine:")
        self.jour_semaine_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(jour_semaine_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.jour_semaine_entry, 0, wx.EXPAND | wx.ALL, 5)

        heure_debut_label = wx.StaticText(form_panel, label="Nouvelle heure de début:")
        self.heure_debut_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(heure_debut_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.heure_debut_entry, 0, wx.EXPAND | wx.ALL, 5)

        heure_fin_label = wx.StaticText(form_panel, label="Nouvelle heure de fin:")
        self.heure_fin_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(heure_fin_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.heure_fin_entry, 0, wx.EXPAND | wx.ALL, 5)

        cours_id_label = wx.StaticText(form_panel, label="Nouveau Cours ID:")
        self.cours_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(cours_id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.cours_id_entry, 0, wx.EXPAND | wx.ALL, 5)

        utilisateur_id_label = wx.StaticText(form_panel, label="Nouveau Utilisateur ID:")
        self.utilisateur_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(utilisateur_id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.utilisateur_id_entry, 0, wx.EXPAND | wx.ALL, 5)

        salle_id_label = wx.StaticText(form_panel, label="Nouveau Salle ID:")
        self.salle_id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(salle_id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.salle_id_entry, 0, wx.EXPAND | wx.ALL, 5)

        button_submit = wx.Button(form_panel, label="Mettre à jour")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_update_emploi)
        form_sizer.Add(button_submit, 0, wx.EXPAND | wx.ALL, 5)
    
    def submit_update_emploi(self, event):
        emploi_id = self.id_entry.GetValue()
        jour_semaine = self.jour_semaine_entry.GetValue()
        heure_debut = self.heure_debut_entry.GetValue()
        heure_fin = self.heure_fin_entry.GetValue()
        cours_id = self.cours_id_entry.GetValue()
        utilisateur_id = self.utilisateur_id_entry.GetValue()
        salle_id = self.salle_id_entry.GetValue()
        
        update_emploidutemps(emploi_id, jour_semaine, heure_debut, heure_fin, cours_id, utilisateur_id, salle_id)
        self.clear_frame(self.emploi_tab)
        self.emploi()  # Update the display after updating the schedule
    
    #  supprimer d'un emploi
    def delete_emploi(self):
        self.clear_frame(self.emploi_tab)

        form_panel = wx.Panel(self.emploi_tab)
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_panel.SetSizer(form_sizer)
        self.emploi_tab.GetSizer().Add(form_panel, 1, wx.EXPAND)

        frame_title = wx.StaticText(form_panel, label="Supprimer l'emploi du temps")
        frame_title.SetFont(wx.Font(wx.FontInfo(12).Bold()))
        form_sizer.Add(frame_title, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        id_label = wx.StaticText(form_panel, label="ID de l'emploi du temps à supprimer:")
        self.id_entry = wx.TextCtrl(form_panel)
        form_sizer.Add(id_label, 0, wx.EXPAND | wx.ALL, 5)
        form_sizer.Add(self.id_entry, 0, wx.EXPAND | wx.ALL, 5)

        button_submit = wx.Button(form_panel, label="Supprimer")
        button_submit.Bind(wx.EVT_BUTTON, self.submit_delete_emploi)
        form_sizer.Add(button_submit, 0, wx.EXPAND | wx.ALL, 5)

    def submit_delete_emploi(self, event):
        emploi_id = self.id_entry.GetValue()
        delete_emploidutemps(emploi_id)
        self.clear_frame(self.emploi_tab)
        self.emploi()  # Refresh the display after deletion

        
def main():
    app = wx.App()
    frame = App(None, title="Application de gestion d'emploi de temps")
    app.MainLoop()

if __name__ == '__main__':
    main()
