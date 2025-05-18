from scipy.optimize import linprog


# Minimiser : W = 4000*y1 + 3000*y2 + 100*y3
c = [4000, 3000, 100]
# Contraintes du dual :
A = [
    [-20, -10, -0.05],
    [-25, -15, -0.08],
    [-30, -12, -0.10]
]
b = [-2000, -3000, -2500]

bounds = [(0, None), (0, None), (0, None)]

result = linprog(c=c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if result.success:
    print("✅ Résolution terminée avec succès.\n")
    print(f"Valeurs optimales des variables duales :")
    print(f"y1 (développement)     = {result.x[0]:.2f} €/h")
    print(f"y2 (gestion de projet) = {result.x[1]:.2f} €/h")
    print(f"y3 (serveurs)          = {result.x[2]:.2f} €/To")
    print(f"\nValeur optimale de W* (minimisation) = {result.fun:.2f} €")
else:
    print("❌ Échec de la résolution :", result.message)
