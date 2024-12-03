a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the value of constant: "))

disc = ((b**2) - (4*a*c)) 

if disc >= 0:
    disc_root = disc ** (1/2)

    root_1 = (-b + disc_root) / (2*a)
    root_2 = (-b - disc_root) / (2*a)

    print("The roots of Q.E are:", root_1, "and", root_2)
else:
    print("The roots are imaginary!")