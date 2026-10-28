from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# Zaid Pharma Database
ZAID_DRUG_DB = {
    "paracetamol": {
        "use": "बुखार और दर्द निवारक (Antipyretic & Analgesic)",
        "dose": "500mg - 650mg (दिन में अधिकतम 3-4 बार)",
        "category": "Analgesic",
        "botanical": "Synthetic derivative of aniline"
    },
    "amoxicillin": {
        "use": "बैक्टीरियल इन्फेक्शन (गला, कान, छाती)",
        "dose": "डॉक्टर की सलाह अनुसार (250mg - 500mg)",
        "category": "Antibiotic (Penicillin group)",
        "botanical": "Semi-synthetic penicillin"
    },
    "cetirizine": {
        "use": "एलर्जी, सर्दी, छींक और बहती नाक",
        "dose": "10mg दिन में एक बार (रात में)",
        "category": "Antihistamine",
        "botanical": "Synthetic piperazine derivative"
    },
    "omeprazole": {
        "use": "एसिडिटी, सीने में जलन और गैस",
        "dose": "20mg सुबह खाली पेट",
        "category": "Proton Pump Inhibitor (PPI)",
        "botanical": "Synthetic benzimidazole derivative"
    },
    "aspirin": {
        "use": "हल्का दर्द निवारक और ब्लड थिनर",
        "dose": "75mg से 325mg निर्देशानुसार",
        "category": "NSAID / Antiplatelet",
        "botanical": "Willow bark (सैलिसिलेट)"
    }
}

class ZaidApp(App):
    def build(self):
        # मुख्य लेआउट
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # ऐप का नाम
        title = Label(
            text="[b]Zaid Pharma AI[/b]", 
            markup=True, 
            font_size='22sp', 
            size_hint=(1, 0.12)
        )
        root.add_widget(title)
        
        # इनपुट बॉक्स
        self.search_input = TextInput(
            hint_text="दवा का नाम लिखें (जैसे paracetamol)",
            multiline=False,
            size_hint=(1, 0.12)
        )
        root.add_widget(self.search_input)
        
        # सर्च बटन
        search_btn = Button(
            text="खोजें (Search)",
            size_hint=(1, 0.12)
        )
        search_btn.bind(on_press=self.search_drug)
        root.add_widget(search_btn)
        
        # रिज़ल्ट दिखाने का बॉक्स
        scroll = ScrollView(size_hint=(1, 0.64))
        self.result_label = Label(
            text="यहाँ दवा की जानकारी दिखाई देगी...",
            font_size='16sp',
            markup=True
        )
        scroll.add_widget(self.result_label)
        root.add_widget(scroll)
        
        return root

    def search_drug(self, instance):
        query = self.search_input.text.strip().lower()
        if not query:
            self.result_label.text = "कृपया किसी दवा का नाम लिखें।"
            return
            
        drug = ZAID_DRUG_DB.get(query)
        if drug:
            info = (
                f"[b]दवा:[/b] {query.upper()}\n\n"
                f"[b]उपयोग:[/b] {drug['use']}\n\n"
                f"[b]खुराक:[/b] {drug['dose']}\n\n"
                f"[b]वर्ग:[/b] {drug['category']}\n\n"
                f"[b]स्रोत:[/b] {drug['botanical']}"
            )
            self.result_label.text = info
        else:
            self.result_label.text = f"'{query}' डेटाबेस में नहीं मिली।\n(paracetamol, aspirin, cetirizine आदि ट्राय करें)"

if __name__ == '__main__':
    ZaidApp().run()
