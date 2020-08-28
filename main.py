#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter

from graphql_client import query
from type import Problem


def get_args():
    parser = argparse.ArgumentParser(description='a leetcode problem info crawler',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-p', '--problem', required=True, nargs='+', action='store', help='the problem you want to get')
    args = parser.parse_args()
    return args


def query_problem(problem):
    query_str = """
                query questionData($titleSlug: String!) {
                    question(titleSlug: $titleSlug){
                        questionId
                        questionFrontendId
                        boundTopicId
                        title
                        titleSlug
                        content
                        translatedTitle
                        translatedContent
                        isPaidOnly
                        difficulty
                        likes
                        dislikes
                        isLiked
                        similarQuestions
                        topicTags {
                            name
                            slug
                            translatedName
                            __typename
                        }
                        companyTagStats
                    }
                }
                """
    result = query(problem, query_str)
    return result


def main():
    name = 'valid-number'
    problem = Problem(name)
    p = query_problem(name)
    problem.set_number(p)
    problem.set_is_paid_only(p)
    problem.set_difficulty(p)
    problem.set_likes(p)
    problem.set_dislikes(p)
    problem.set_topic_tags(p)


def set_topic_tags(self, _p):
    self.topic_tags = [i['name'] for i in _p['question']['topicTags']]


if __name__ == '__main__':
    main()
