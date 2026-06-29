func groupAnagrams(strs []string) [][]string {
    var encLetters [26]int
    groups := make(map[[26]int][]string)

    for _, str := range strs {
        encLetters = [26]int{}
        for _, c := range str {
            // fmt.Println(string(c), c - 'a')
            index := c - 'a'
            encLetters[index]++
        }

        groups[encLetters] = append(groups[encLetters], str)
        // fmt.Println(groups)
    }

    var res [][]string
    for _, group := range groups {
        res = append(res, group)
    }

    return res
}
