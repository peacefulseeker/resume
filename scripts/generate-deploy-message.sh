#!/bin/bash
# scripts/generate-deploy-message.sh
# Script to generate dynamic commit messages with fallback for empty messages

# Extract basic commit info
COMMIT_HASH=$(git rev-parse --short HEAD)
COMMIT_MSG=$(git log -1 --pretty=%s)
COMMIT_AUTHOR=$(git log -1 --pretty=%an)

# Check if this is a merge commit (has 2+ parents)
PARENT_COUNT=$(git rev-list --count --parents -n 1 HEAD | awk '{print NF-1}')

if [ "$PARENT_COUNT" -gt "1" ]; then
  # It's a merge commit, try to extract PR number
  PR_NUMBER=$(echo "$COMMIT_MSG" | grep -oE 'pull request #[0-9]+' | grep -oE '#[0-9]+')

  if [ ! -z "$PR_NUMBER" ]; then
    # Found PR reference in commit message
    DEPLOY_MSG="Deploy from PR ${PR_NUMBER}: ${COMMIT_MSG} (${COMMIT_HASH})"
  else
    # Merge commit but no PR number found
    DEPLOY_MSG="Deploy from merge: ${COMMIT_MSG} (${COMMIT_HASH})"
  fi
else
  # Regular commit
  DEPLOY_MSG="Deploy: ${COMMIT_MSG} (${COMMIT_HASH}, by ${COMMIT_AUTHOR})"
fi

# Check if message is empty and provide fallback if needed
if [ -z "$DEPLOY_MSG" ]; then
  echo "Deploy: Update resume (${COMMIT_HASH}, by ${COMMIT_AUTHOR})"
else
  echo "$DEPLOY_MSG"
fi
