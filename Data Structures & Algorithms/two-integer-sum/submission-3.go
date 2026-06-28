func twoSum(nums []int, target int) []int {
    // key is nums value and value is index of nums
    hash := make(map[int]int)
    
    for i := 0; i < len(nums); i++ {
        if val, ok := hash[target - nums[i]]; ok == true {
            return []int{val, i}
        }
        hash[nums[i]] = i
        // fmt.Println(hash)
    }

    return nil
}
