import itertools
def read_calibration(filename):
    f=open(filename)
    results=[]
    parameters=[]
    for line in f:
        split=line.split(":")
        results.append(int(split[0]))
        splitnumbers=split[1].split()
        splitnumbers=[int(sn) for sn in splitnumbers]
        parameters.append(splitnumbers)

    return results, parameters

def build_operation_matrix(operations, num_params):
    table=list(itertools.product(operations, repeat=num_params))
    return table


def test_equation(result, parameters, operation_matrix):

    for operations in operation_matrix:
        sum=parameters[0]
        for op,pa in zip(operations, parameters[1:]):
            if op=="+":
                sum=sum+pa
            elif op=="*":
                sum=sum*pa
            elif op=="|":
                sum=int(str(sum)+str(pa))
        if sum-result==0:
            return result
    return 0
    


if __name__ == "__main__":
    results, parameters=read_calibration("day7.txt")
    operations=["+","*", "|"]
    used_param_lengths=[]
    operation_matrices=[]
    good_result_sum=0
    for result,params in zip(results,parameters):
        if len(params) in used_param_lengths:
            operation_matrix=operation_matrices[used_param_lengths.index(len(params))]
        else:
            operation_matrix=build_operation_matrix(operations, len(params)-1)
            used_param_lengths.append(len(params))
            operation_matrices.append(operation_matrix)

        good_result_sum+=test_equation(result, params, operation_matrix)



    print(good_result_sum)

    