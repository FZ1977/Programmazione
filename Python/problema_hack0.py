def solve(K: int) -> int:
        """
        Scrivi la tua soluzione qui.
        """
        x = K//2
        z = K//2
        y = (K - z)/x
        print(int(x)," ",int(y)," ",int(z))
        pass


solve(1254)
