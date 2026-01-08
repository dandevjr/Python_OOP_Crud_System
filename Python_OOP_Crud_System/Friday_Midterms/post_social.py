class Post:
    def __init__(self, username, content):
        self.username = username              # PUBLIC ATTRIBUTE
        self.content = content                # PUBLIC ATTRIBUTE
        self.__likeCount = 0                  # PRIVATE ATTRIBUTE
        self.__reportCount = 0                # PRIVATE ATTRIBUTE

    def add_like(self):
        self.__likeCount += 1

    def report_post(self):
        self.__reportCount += 1

    def get_likes(self):
        return self.__likeCount

    def get_reports(self):
        return self.__reportCount

    def display_post(self):
        print(f"User: {self.username}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.__likeCount}")
        print(f"Reports: {self.__reportCount}")

    def update_content(self, new_content):
        self.content = new_content
        print("Post content updated.")

# OBJECT CREATION: sample post
posts = {
    "SamplePost": Post("Nullroot", "Building resilient systems for Tacloban.")
}

# MAIN MENU LOOP
while True:
    print("\nPOST MANAGEMENT SYSTEM")
    print("1. Create Multiple Posts")
    print("2. View All Posts")
    print("3. Like a Post")
    print("4. Report a Post")
    print("5. Update Post Content")
    print("6. Delete a Post")
    print("7. Encapsulation Test")
    print("8. Exit")

    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        count = int(input("How many posts do you want to create? "))
        for i in range(count):
            print(f"\nCreating post {i+1} of {count}")
            key = input("Enter post ID: ")
            if key in posts:
                print("Post ID already exists.")
            else:
                username = input("Enter username: ")
                content = input("Enter post content: ")
                posts[key] = Post(username, content)
                print(f"Post '{key}' created.")

    elif choice == "2":
        print("\nAll Posts:")
        if not posts:
            print("No posts available.")
        else:
            for key, post in posts.items():
                print(f"\nPost ID: {key}")
                post.display_post()

    elif choice == "3":
        key = input("Enter post ID to like: ")
        if key in posts:
            posts[key].add_like()
            print("Post liked.")
        else:
            print("Post not found.")

    elif choice == "4":
        key = input("Enter post ID to report: ")
        if key in posts:
            posts[key].report_post()
            print("Post reported.")
        else:
            print("Post not found.")

    elif choice == "5":
        key = input("Enter post ID to update: ")
        if key in posts:
            new_content = input("Enter new content: ")
            posts[key].update_content(new_content)
        else:
            print("Post not found.")

    elif choice == "6":
        key = input("Enter post ID to delete: ")
        if key in posts:
            del posts[key]
            print(f"Post '{key}' deleted.")
        else:
            print("Post not found.")

    elif choice == "7":
        print("\nEncapsulation Test:")
        for key, post in posts.items():
            print(f"\nPost ID: {key}")
            try:
                post.__likeCount = 1000
                print("Direct likeCount set to 1000.")
            except:
                print("Failed to set likeCount directly.")
            try:
                post.__reportCount = -5
                print("Direct reportCount set to -5.")
            except:
                print("Failed to set reportCount directly.")
            print(f"Likes (via method): {post.get_likes()}")
            print(f"Reports (via method): {post.get_reports()}")

       
    elif choice == "8":
        print("Exiting post system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")