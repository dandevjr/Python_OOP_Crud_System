class Post:
    def __init__(self, post_id, username, content):
        self.post_id = post_id        
        self.username = username      
        self.content = content        
        self.__likeCount = 0          
        self.__reportCount = 0         
   
    def addLike(self):
        self.__likeCount += 1
        print(f" Post #{self.post_id} by {self.username} got a new like! Total Likes: {self.__likeCount}")

    def reportPost(self):
        self.__reportCount += 1
        print(f" Post #{self.post_id} by {self.username} was reported! Total Reports: {self.__reportCount}")

   
    def getLikes(self):
        return self.__likeCount

    def getReports(self):
        return self.__reportCount

    def showPost(self):
        print(f"\n Post ID: {self.post_id}")
        print(f" User: {self.username}")
        print(f" Content: {self.content}")
        print(f" Likes: {self.__likeCount} |  Reports: {self.__reportCount}")



posts = {}

while True:
    print("\n=== SOCIAL MEDIA POST SYSTEM ===")
    print("1. Create a Post")
    print("2. View All Posts")
    print("3. Like a Post")
    print("4. Report a Post")
    print("5. Try to Cheat (Modify Private Variables)")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter username: ")
        content = input("Enter post content: ")
        post_id = len(posts) + 1
        posts[post_id] = Post(post_id, username, content)
        print(f" Post #{post_id} created successfully!")
        print(f" You can reference your post using ID #{post_id}.")

    elif choice == '2':
        if not posts:
            print("No posts available yet.")
        else:
            print("\n--- Current Posts ---")
            for post in posts.values():
                post.showPost()

    elif choice == '3':
        if not posts:
            print("No posts available to like.")
        else:
            post_id = int(input("Enter post ID to like: "))
            if post_id in posts:
                posts[post_id].addLike()
            else:
                print(" Invalid post ID!")

    elif choice == '4':
        if not posts:
            print("No posts available to report.")
        else:
            post_id = int(input("Enter post ID to report: "))
            if post_id in posts:
                posts[post_id].reportPost()
            else:
                print(" Invalid post ID!")

    elif choice == '5':
        print("\n--- Encapsulation Demonstration ---")
        demo = Post(999, "DemoUser", "This is a test post.")
        demo.showPost()

        print("\nAttempting to cheat by directly setting likeCount and reportCount...")
        demo.__likeCount = 999
        demo.__reportCount = 999
        print("Cheat applied!")

        print("\nNow displaying post again:")
        demo.showPost()

        print("\n Why cheat fails:")
        print("Because __likeCount and __reportCount are private attributes.")
        print("Python automatically renames them internally (name mangling).")
        print("Assigning demo.__likeCount = 999 just creates *new* public variables,")
        print("while the real private counters remain unchanged inside the object.")

    elif choice == '6':
        print(" Exiting Social Media App Simulation. Goodbye!")
        break

    else:
        print(" Invalid choice. Try again.")
