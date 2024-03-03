from tabulate import tabulate

class Service:
    def __init__(self, title, net, vat):
        self.title = title
        self.net = net
        self.vat = vat

    def totalNet():
        sumNet = 0
        for i in services:
            sumNet += i.net
        return sumNet
    
    def totalVat():
        sumVat1 = 0
        sumVat2 = 0
        for i in services:
            if i.vat == services[0].vat:
                sumVat1 += i.vat*i.net
            else:
                sumVat2 += i.vat*i.net
        return sumVat1, sumVat2
    
    def markdown():
        a = Service.totalNet()
        b = Service.totalVat()
        head = ["", "Total net", "X"]
        mydata = [["VAT 8%", a, b[0]], ["VAT 23%", a, b[1]]]
        print(tabulate(mydata, headers=head, tablefmt = "simple_grid", numalign="center"))

        # Solution to be used without tabulate module installed (uncomment to use)
        """
        print(f'''
        |          |  Total net  |    X    |
        |----------|-------------|---------|
        | VAT 8%   |    {a}    |  {b[0]}   |
        | VAT 23%  |    {a}    |  {b[1]}   |
        ''')
        """
        
p1 = Service("Clean Code, Robert C. Martin", 100.00, 0.08)
p2 = Service("Applying UML and Patterns, C. Larman", 300.00, 0.08)
p3 = Service("Shipping", 50, 0.23)

services = [p1, p2, p3]

Service.markdown()