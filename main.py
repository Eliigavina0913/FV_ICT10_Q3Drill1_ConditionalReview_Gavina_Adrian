from pyscript import document

("click", "#computebtn")
def get_average(event=None): 
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    s1 = max(0, min(100, float(s1))) if s1  else "error"
    s2 = max(0, min(100, float(s2))) if s2 else "error"

    avg = (float(s1) + float(s2)) / 2

    document.getElementById("get_average").innerText = f"Average: {avg:.2f}"
    if avg >= 75:
        document.getElementById("result").innerText = f"✅ Passed!: {avg:.2f}"
    
    else:
        document.getElementById("result").innerText = f"❌ Failed!: {avg:.2f}"
