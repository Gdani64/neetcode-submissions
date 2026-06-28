func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    var convertedStr []rune 
    for _, str := range strs {
        // fmt.Println(str)
        convertedStr = []rune(str)
        sort.Slice(convertedStr, func(i, j int) bool {
            return convertedStr[i] < convertedStr[j] // Increasing order
        })
        
        groups[string(convertedStr)] = append(groups[string(convertedStr)], str)
    }

    var res [][]string
    for _, v := range groups {
        res = append(res, v)
    }

    return res
}
