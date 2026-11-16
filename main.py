from pyscript import display, document

members = {
    "A": ["Abby", "Aura", "Apple", "Amo"],
    "B": ["Bob", "Bolt", "Braze", "Bolb"],
    "C": ["Crate", "Craze", "Cook", "Caul"],
    "D": ["Darren", "Dave", "Dude", "Dog"]
}

def submit(e):
    document.getElementById("result").innerHTML = ""

    member_name = document.getElementById("fname").value.strip().title()

    result = members.get(member_name, ("Member not found", "-", "-", "-","Blu.jpg"))

    document.getElementById("result").innerHTML = f"""
    <b> First: </b>  {member_name}<br>
    <b> Second: </b>  {result[0]}<br>
    <b> Third: </b>  {result[1]}<br>
    <b> Fourth: </b> {result[2]} 
    """
