class analysis_assumptions:
    def __init__(self):
        self.no_dependent_variables = int(input("NUMBER OF DEPENDENT VARIABLES"))
        self.no_independent_variables = int(input("NUMBER OF INDEPENDENT VARIABLES"))
        self.type_of_dependent_variables = input("TYPE OF DEPENDENT VARIABLES")
        self.type_of_independent_variables = input("TYPE OF INDEPENDENT VARIABLES")

        self.analise()



    def analise(self):

        if self.no_dependent_variables == 1:
            if self.no_independent_variables == 0:
                if self.type_of_dependent_variables == "continuous normal":
                    if self.type_of_independent_variables == "none":
                            print("MEASURE: MEAN\n"
                            "TEST: ONE SAMPLE T-TEST ")

                elif self.type_of_dependent_variables == "continuous non-normal":
                    if self.type_of_independent_variables == "none":
                        print("MEASURE: MEDIAN\n"
                              "TEST: ONE SAMPLE MEDIAN")
                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "none":
                        print("MEASURE: PROPORTIONS:"
                              "TEST: CHI SQUARE GOODNESS OF FIT\n"
                              "      BINOMIAL TEST")
        if self.no_dependent_variables == 1:
            if self.no_independent_variables == 1:
                print("PROBABLY TWO INDEPENDENT POPULATIONS")
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "two categories":
                        print("MEASURE: MEAN\n"
                              "TEST : 2 INDEPENDENT SAMPLE T-TEST")
                elif self.type_of_dependent_variables == "non-normal":
                    if self.type_of_independent_variables == "two categories":
                        print("MEASURE: MEDIANS\n"
                              "TEST : MANN WHITNEY\n"
                              "       WILCOXON RANK SUM TEST")

                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "two categories":
                        print("MEASURE: PROPORTIONS"
                              "TEST: CHI-SQUARE TEST\n"
                              "FISHER'S EXACT TEST")



        if self.no_dependent_variables ==  1:
            if self.no_independent_variables == 0 or 1:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "none" or "categorical":
                        print("MEASURES: MEAN\n"
                              "TEST: PAIRED T-TEST")
                elif self.type_of_dependent_variables == "non-normal":
                    if self.type_of_independent_variables == "none" or "categorical":
                        print("MEASURES: MEDIANS\n"
                              "TEST: WILCOXON SIGNED RANK TEST")

                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "none" or "categorical":
                        print("MEASURES: PROPORTIONS\n"
                              "TEST: McNEMAR\n"
                              "      CHI-SQUARE")


        if self.no_dependent_variables == 1:
            if self.no_independent_variables == 1:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: MEANS\n"
                              "TEST: ONE WAY ANALYSIS OF VARIANCE (ANOVA")
                elif self.type_of_dependent_variables == "non-normal":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: MEDIANS\n"
                              "TEST: KRUSKAL WALIS")

                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: PROPORTIONS\n"
                              "TEST: CHI-SQUARE TEST")

        if self.no_dependent_variables == 1:
            if self.no_independent_variables >= 2:
                if self.type_of_dependent_variables =="normal":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: MEAN\n"
                              "TEST: FACTORIAL ANOVA")

                elif self.type_of_dependent_variables == "non-normal":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: MEDIANS\n"
                              "TEST: FRIEDMAN TEST ")
                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURES: PROPORTIONS\n"
                              "TEST: LOG-LINEAR\n"
                              "      LOGISTIC REGRESSION")

        if self.no_dependent_variables == 1:
            if self.no_independent_variables == 0:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "none":
                        print("MEASURES: MEAN\n"
                              "TEST: REPEATED MEASURES ANOVA")


        if self.no_dependent_variables == 1:
            if self.no_independent_variables == 1:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST: CORRELATION\n"
                              "      SIMPLE LINEAR REGRESSION")
                    elif self.type_of_dependent_variables == "non-normal":
                        if self.type_of_independent_variables == "continuous":
                            print("MEASURES: NONE AT THE MOMENT\n"
                                  "TEST: NON PARAMETRIC CORRELATION")

                    elif self.type_of_dependent_variables == "categorical":
                        if self.type_of_independent_variables == "categorical" or "continuous":
                            print("MEASURES: NONE AT THE MOMENT\n"
                                  "TEST: LOGISTIC REGRESSION")

                        elif self.type_of_independent_variables == "categorical":
                            print("MEASURES: NONE AT THE MOMENT\n"
                                  "TEST: DISCRIMINANT ANALYSIS")





        if self.no_dependent_variables == 1:
            if self.no_independent_variables >= 2:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST : MULTIPLE LINEAR REGRESSION")
                    elif self.type_of_independent_variables == "mixed categorical + continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST : ANALYSIS OF COVARIANCE\n"
                              "       GENERAL LINEAR MODELS(REGRESSION)")

                elif self.type_of_dependent_variables == "non-normal":
                    if self.type_of_independent_variables == "continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST: NONE AT THE MOMENT")
                    elif self.type_of_independent_variables == "mixed categorical and continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST: NONE AT THE MOMENT")
                elif self.type_of_dependent_variables == "categorical":
                    if self.type_of_independent_variables == "continuous":
                        print("MEASURE: NONE AT THE MOMENT\n"
                              "TEST: LOGICAL REGRESSION")
                    elif self.type_of_independent_variables == "mixed categorical and continuous":
                        print("MEASURE: NONE AT THE MOMENT\n"
                              "TEST: LOGISTIC REGRESSION")

        if self.no_dependent_variables == 2 :
            if self.no_independent_variables >=2 :
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "categorical":
                        print("MEASURE: NONE AT THE MOMENT"
                              "TEST: MULTIVARIATE ANALYSIS OF VARIANCE (MANOVA)")

        if self.no_dependent_variables >= 2:
            if self.type_of_independent_variables >= 2:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "continuous":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST: MULTIVARIATE MULTIPLE LINEAR REGRESSION")


        if self.no_dependent_variables >= 4:
            print("PROBABLY 2 SETS OF 2")
            if self.no_independent_variables == 0:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "none":
                        print("MEASURE: NONE AT THE MOMENT\n"
                              "TEST: CANONICAL CORRELATION")


        if self.no_dependent_variables >= 2:
            if self.no_independent_variables == 0:
                if self.type_of_dependent_variables == "normal":
                    if self.type_of_independent_variables == "none":
                        print("MEASURES: NONE AT THE MOMENT\n"
                              "TEST: FACTOR ANALYSIS")























        else:
            print("nnothing")



if __name__ == "__main__":
    analysis_assumptions()

