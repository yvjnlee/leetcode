class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        # had to look this up via grok
        new_path = [_ for _ in (path.split('/')) if _.strip()]
        res = []

        for i, directory in enumerate(new_path):
            # print(res, directory)
            if directory == '..':
                if res: res.pop()
                continue
            if directory != '.':
                res.append(directory)
            # print(res)
        
        return f"/{'/'.join(res)}" 
