def total_carrito(request):
    total_c = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total_c += int(value["total"])
    return {"total_carrito": total_c}
