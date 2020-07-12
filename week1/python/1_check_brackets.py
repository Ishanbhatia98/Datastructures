def check(s):
    stack = []
    brackets = {'{': '}', '[': ']', '(': ')'}
    if len(s) == 1:
        return 1
    else:
        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append((s[i], i))
            elif s[i] in brackets.values():
                if len(stack) > 0:
                    b, index = stack.pop()
                    if brackets[b] != s[i]:
                        return i+1
                else:
                    return i+1
        if len(stack) == 0:
            return 'Success'
        else:
            b, i = stack.pop()
            return i+1


s = input()

print(check(s))
