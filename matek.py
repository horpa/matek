import argparse
import textwrap

from src.multiplication import practice as p
from src.roman import practice as r


def init_argparse():
    arg_parser = argparse.ArgumentParser(
        prog="matek",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Matek (szorzotabla) gyakorlo",
        epilog=textwrap.dedent(
            """\
            Peldak:
                matek -e=multi 2 3 4 --min=0 --max 12 --req 3
                    "A 2-es 3-as 4-es szorzotablat gyakoroljuk. Legkisebb szorzat a 2*0 a legnagyobb a 4*12.
                    Legalabb 3 helyes valasz kell ahhoz, hogy azt mondjuk mar jol tudod."

                matek --exercise multi --req 3
                    "2*1-tol 2*10-ig gyakoroljuk a 2-es szorotablat. Legalabb 3 jo valasz esetne mondjuk, hogy jol tudod."
                    
                matek -e=roman --min=1 --max=20 --req=6
                    "roman szamok atirasat gyakoroljuk 1-tol 20-ig, ugy, hogy legalabb mindegyik szamhoz tartozo
                    feladatokbol jol meg kell oldani 6-ot."
            """
        ),
    )

    arg_parser.add_argument(
        "-e",
        "--exercise",
        choices=["multi", "roman"],
        default="multi",
        help="milyen feladatot szeretnél gyakorolni",
    )
    arg_parser.add_argument(
        "base_numbers",
        metavar="B",
        nargs="*",
        default=[2],
        help="melyik szorzotabla(ka)t szeretned gyakoroltatni. Adj meg tobbet szokozzel elvalasztva."
        "Alapertelmezes szerint csak a 2-es szorzotablat gyakoroljuk.",
    )
    arg_parser.add_argument(
        "--min",
        type=int,
        default=1,
        help="A szorzotablat ettol kezdve gyakoroljuk. Ha nem mondasz mast, akkor 1-tol.",
    )
    arg_parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="A szorzotablat eddig gyakoroljuk. Ha nem mondasz mast, akkor 10-ig.",
    )
    arg_parser.add_argument(
        "--req",
        type=int,
        default=5,
        help="legalabb hany jo valaszt kell adni, hogy azt mondjuik mar jol tudod az adott szorzast."
        "Alapertelmezes szarint 5-ot",
    )
    return arg_parser


if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()

    if args.exercise == "multi":
        p.practice_multiplication(args.min, args.max, args.req, args.base_numbers)
    if args.exercise == "roman":
        r.practice_roman_numerals(args.min, args.max, args.req)
