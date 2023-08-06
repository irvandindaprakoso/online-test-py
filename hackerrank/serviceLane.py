def service_lane(cases, width):
    # Write your code here
    result = []
    for i,j in cases:
        result.append(min(width[i: j+1]))
    return result