from unittest import TestCase, main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.profile = SocialMedia("Teodor", "Instagram", 100, "blog")


    def test_correct_init(self):
        self.assertEqual(self.profile._username, "Teodor")
        self.assertEqual(self.profile._platform, "Instagram")
        self.assertEqual(self.profile._followers, 100)
        self.assertEqual(self.profile._content_type, "blog")
        self.assertEqual(self.profile._posts, [])

    def test_platform_validation(self):
        # Test with a valid platform
        profile = SocialMedia("Teodor", "Instagram", 100, "blog")
        self.assertEqual(profile._platform, "Instagram")

        # Test with an invalid platform
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as context:
            SocialMedia("Teodor", "InvalidPlatform", 100, "blog")
        self.assertEqual(str(context.exception), f"Platform should be one of {allowed_platforms}")
        
    
    def test_platform_getter(self):
        self.assertEqual(self.profile.platform, "Instagram")


    def test_platform_setter_valid(self):
        self.profile.platform = "YouTube"
        self.assertEqual(self.profile.platform, "YouTube")


    def test_platform_setter_invalid(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as context:
            self.profile.platform = "InvalidPlatform"
        self.assertEqual(str(context.exception), f"Platform should be one of {allowed_platforms}")

    
    def test_followers_setter_valid(self):
        self.profile.followers = 1
        self.assertEqual(self.profile.followers, 1)

    def test_followers_setter_invalid(self):
        # Test with negative followers
        with self.assertRaises(ValueError) as context:
            self.profile.followers = -1
        self.assertEqual(str(context.exception), "Followers cannot be negative.")


    def test_create_post(self):
    # Test post creation
        initial_posts_count = len(self.profile._posts)
        post_content = "This is a test post."
        self.profile.create_post(post_content)
        self.assertEqual(len(self.profile._posts), initial_posts_count + 1)
        self.assertEqual(self.profile._posts[0]['content'], post_content)
        self.assertEqual(self.profile._posts[0]['likes'], 0)
        self.assertEqual(self.profile._posts[0]['comments'], [])
        self.assertEqual(
            self.profile.create_post(post_content),
            f"New blog post created by Teodor on Instagram."
        )


    def test_like_post(self):
    # Create a post
        post_content = "This is a test post."
        self.profile.create_post(post_content)

        # Test liking a post
        initial_likes = self.profile._posts[0]['likes']
        self.assertEqual(self.profile.like_post(0), f"Post liked by Teodor.")
        self.assertEqual(self.profile._posts[0]['likes'], initial_likes + 1)

        # Test reaching maximum likes
        for _ in range(9 - initial_likes):  # Change here
            self.assertEqual(self.profile.like_post(0), f"Post liked by Teodor.")
        self.assertEqual(self.profile.like_post(0), f"Post has reached the maximum number of likes.")

        # Test invalid post index
        self.assertEqual(self.profile.like_post(1), "Invalid post index.")

    
    def test_comment_on_post(self):
    # Create a post
        post_content = "This is a test post."
        self.profile.create_post(post_content)

        # Test adding a comment
        comment = "This is a test comment which is more than 10 characters."
        self.assertEqual(self.profile.comment_on_post(0, comment), f"Comment added by Teodor on the post.")
        self.assertEqual(self.profile._posts[0]['comments'][-1], {'user': 'Teodor', 'comment': comment})

        # Test comment length requirement
        short_comment = "Short"
        self.assertEqual(self.profile.comment_on_post(0, short_comment), "Comment should be more than 10 characters.")





if __name__ == '__main__':
    main()